from math import acos, atan2, pi 
import numpy as np

from arena.map import Map
from common.consts import ROBOT_TURNING_RADIUS
from common.enums import TurnDirection, Path, Movement
from common.types import Position
from common.utils import calc_vector, rotate_vector
from path_finding.path_validation import has_collision


class PathParams:
    """Stores info about a Dubins path"""

    def __init__(
        self,
        type: "Path",
        p1: np.array,
        p2: np.array,
        pt1: np.array,
        pt2: np.array,
        arc1: float,
        s: float,
        arc2: float
    ):
        self.type = type
        self.p1 = p1
        self.p2 = p2
        self.pt1 = pt1
        self.pt2 = pt2
        self.arc1 = arc1
        self.s = s
        self.arc2 = arc2
        self.len = arc1 + s + arc2


    def __str__(self) -> str:
        return f'{self.type}\np1: {self.p1}, p2: {self.p2}\npt1: {self.pt1}, pt2: {self.pt2}\narc1: {self.arc1:.2f}, s: {self.s:.2f}, arc2: {self.arc2:.2f}, len: {self.len:.2f}\n'


# movements = {
#     (1, -1): Movement.FWD_LEFT,
#     (1, 0): Movement.FWD,
#     (1, 1): Movement.FWD_RIGHT,
#     (-1, -1): Movement.BWD_LEFT,
#     (-1, 0): Movement.BWD,
#     (-1, 1): Movement.BWD_RIGHT
# }


class DubinsPath:

    def shortest_path(
        self, 
        st: "Position",
        end: "Position",
        mp: "Map"
    ) -> "Path | None":
        
        mn_path = None
        mn_len = float('inf')

        for path in self._find_paths(st, end):
            if path.type == Path.LSL:
                dirs = Movement.FWD_LEFT, Movement.FWD_LEFT
            elif path.type == Path.LSR:
                dirs = Movement.FWD_LEFT, Movement.FWD_RIGHT
            elif path.type == Path.RSR:
                dirs = Movement.FWD_RIGHT, Movement.FWD_RIGHT
            elif path.type == Path.RSL:
                dirs = Movement.FWD_RIGHT, Movement.FWD_LEFT
            else:
                continue


            if has_collision(st, path.arc1, dirs[0], mp):
                continue

            theta1 = (st.theta + path.arc1 / ROBOT_TURNING_RADIUS) % (2 * pi)
            if has_collision(
                Position(
                    path.pt1[0], 
                    path.pt1[1], 
                    theta1,
                ), 
                path.s, 
                Movement.FWD, 
                mp
            ):
                continue

            if has_collision(
                Position(
                    path.pt1[0], 
                    path.pt1[1], 
                    (theta1 + path.arc2 / ROBOT_TURNING_RADIUS) % (2 * pi)
                ),
                path.arc2, 
                dirs[1], 
                mp
            ):
                continue
            
            if path.len < mn_len:
                mn_len = path.len
                mn_path = path

        return mn_path


    def _find_paths(
        self,
        st: "Position",
        end: "Position"
    ):
        self.s = np.array([st.x, st.y])
        self.e = np.array([end.x, end.y])

        self.lc1 = calc_vector(st.theta + pi/2, ROBOT_TURNING_RADIUS)
        self.lc2 = calc_vector(end.theta + pi/2, ROBOT_TURNING_RADIUS)
        self.rc1 = -self.lc1
        self.rc2 = -self.lc2

        solns = [self._LSL(), self._RSR(), self._LSR(), self._RSL()]

        return solns
    
    
    def _directional_theta(
        self, 
        v1: np.array, 
        v2: np.array,
        direction: "TurnDirection"
    ) -> float:
        theta = atan2(*v1) - atan2(*v2)

        if theta < 0 and direction == TurnDirection.ANTICLOCKWISE:
            theta += 2 * pi
        elif theta > 0 and direction == TurnDirection.CLOCKWISE:
            theta -= 2 * pi
        return theta
    

    def _arc_len(
        self,
        theta: float
    ) -> float:
        return 2 * pi * ROBOT_TURNING_RADIUS * abs(theta) / 2 / pi
        
    
    def _LSL(self):
        v = (self.e + self.lc2) - (self.s + self.lc1)
        m = np.linalg.norm(v)
        vn = ROBOT_TURNING_RADIUS / m * np.array([v[1], -v[0]]) # rotate 90 deg counter clockwise
        
        pt1 = self.s + self.lc1 + vn
        pt2 = self.e + self.lc2 + vn

        theta1 = self._directional_theta(-self.lc1, vn, TurnDirection.ANTICLOCKWISE)
        theta2 = self._directional_theta(vn, -self.lc2, TurnDirection.ANTICLOCKWISE)

        arc1 = self._arc_len(theta1)
        arc2 = self._arc_len(theta2)
        
        return PathParams(
            Path.LSL,
            self.s + self.lc1,
            self.e + self.lc2, 
            pt1,
            pt2,
            arc1,
            m,
            arc2
        )
    
    def _RSR(self):
        v = (self.e + self.rc2) - (self.s + self.rc1)
        m = np.linalg.norm(v)
        vn = ROBOT_TURNING_RADIUS / m * np.array([-v[1], v[0]]) # rotate 90 deg clockwise
        
        pt1 = self.s + self.rc1 + vn
        pt2 = self.e + self.rc2 + vn

        theta1 = self._directional_theta(-self.rc1, vn, TurnDirection.CLOCKWISE)
        theta2 = self._directional_theta(vn, -self.rc2, TurnDirection.CLOCKWISE)

        arc1 = self._arc_len(theta1)
        arc2 = self._arc_len(theta2)
        
        return PathParams(
            Path.RSR,
            self.s + self.rc1,
            self.e + self.rc2, 
            pt1,
            pt2,
            arc1,
            m,
            arc2
        )
    
    def _LSR(self):
        v = (self.e + self.rc2) - (self.s + self.lc1)
        m = np.linalg.norm(v)
        d = (m**2 + (ROBOT_TURNING_RADIUS*2)**2)**0.5

        phi = acos(2*ROBOT_TURNING_RADIUS/m)
        v1n = ROBOT_TURNING_RADIUS / m * rotate_vector(v, -phi)
        v2n = ROBOT_TURNING_RADIUS / m * rotate_vector(-v, -phi)
        
        pt1 = self.s + self.lc1 + v1n
        pt2 = self.e + self.rc2 + v2n

        theta1 = self._directional_theta(-self.lc1, v1n, TurnDirection.ANTICLOCKWISE)
        theta2 = self._directional_theta(v2n, -self.rc2, TurnDirection.CLOCKWISE)

        arc1 = self._arc_len(theta1)
        arc2 = self._arc_len(theta2)
        
        return PathParams(
            Path.LSR,
            self.s + self.lc1,
            self.e + self.rc2,
            pt1,
            pt2,
            arc1,
            d, 
            arc2
        )
    
    def _RSL(self):
        v = (self.e + self.lc2) - (self.s + self.rc1)
        m = np.linalg.norm(v)
        d = (m**2 + (ROBOT_TURNING_RADIUS*2)**2)**0.5

        phi = acos(2*ROBOT_TURNING_RADIUS/m)
        v1n = ROBOT_TURNING_RADIUS / m * rotate_vector(v, phi)
        v2n = ROBOT_TURNING_RADIUS / m * rotate_vector(-v, phi)
        
        pt1 = self.s + self.rc1 + v1n
        pt2 = self.e + self.lc2 + v2n

        theta1 = self._directional_theta(-self.rc1, v1n, TurnDirection.CLOCKWISE)
        theta2 = self._directional_theta(v2n, -self.lc2, TurnDirection.ANTICLOCKWISE)

        arc1 = self._arc_len(theta1)
        arc2 = self._arc_len(theta2)
        
        return PathParams(
            Path.RSL,
            self.s + self.rc1,
            self.e + self.lc2,
            pt1,
            pt2,
            arc1,
            d, 
            arc2
        )