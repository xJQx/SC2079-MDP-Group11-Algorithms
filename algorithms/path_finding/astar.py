import heapq
from math import pi
import numpy as np
import logging
from typing import List, Optional
import time

from arena.map import Map
from common.consts import (
    DIST_BL, 
    DIST_BR, 
    DIST_BW, 
    DIST_FL, 
    DIST_FR, 
    DIST_FW,
    PENALTY_STOP,
    MAX_THETA_ERR,
    MAX_X_ERR,
    MAX_Y_ERR,
    MAP_WIDTH,
    MAP_HEIGHT,
)
from common.enums import Movement
from common.types import Position
from common.utils import calc_vector, euclidean
from path_finding.path_validation import has_collision
from robot.move import (
    bwd,
    bwd_left, 
    bwd_right, 
    fwd, 
    fwd_left, 
    fwd_right
)


logger = logging.getLogger('ASTAR')


class Node:

    def __init__(
        self,
        pos: Position,
        c_pos: Position,
        g: float,
        h: float,
        parent: Optional["Node"] = None,
        v: Optional[int] = 1,
        s: Optional[int] = 0,
        d: Optional[float] = 0
    ):
        self.pos = pos
        self.c_pos = c_pos # pos in continuous scale
        self.g = g # st to curr
        self.h = h # curr to end
        self.f = g + h # total

        self.v = v # prev motion's vert direction, -1: bwd, 1: fwd
        self.s = s # prev motion's steering direction, -1: left, 0: straight, 1: fwd
        self.d = d # dist

        self.parent = parent


    def clone(self) -> "Node":
        return Node(self.pos, self.c_pos, self.g, self.h, self.parent, self.v, self.s, self.d)
    

    def __eq__(
        self,
        node: "Node"
    ) -> bool:
        return self.pos.x == node.pos.x and \
            self.pos.y == node.pos.y and \
            self.pos.theta == node.pos.theta


    def __lt__(
        self, 
        node: "Node"
    ) -> bool:
        # custom comparator for heapq
        return self.f < node.f
    

    def __str__(self) -> str:
        return f'Node(x:{self.c_pos.x:6.2f}, y:{self.c_pos.y:6.2f}, θ:{self.c_pos.theta:6.2f}, g:{self.g:6.2f}, h:{self.h:6.2f}, f:{self.f:6.2f}), v:{self.v}, s:{self.s}'


class AStar:

    def __init__(
        self, 
        mp: "Map"
    ):
        # self.moves: (v, s, d, Movement, movement function); See `Node` __init__ for definitions of the respective variables
        self.moves = (
            ( 1,  0, DIST_FW,    Movement.FWD,       fwd),
            ( 1, -1, DIST_FL[2], Movement.FWD_LEFT,  fwd_left),
            ( 1,  1, DIST_FR[2], Movement.FWD_RIGHT, fwd_right),
            (-1,  0, DIST_BW,    Movement.BWD,       bwd),
            (-1, -1, DIST_BL[2], Movement.BWD_LEFT,  bwd_left),
            (-1,  1, DIST_BR[2], Movement.BWD_RIGHT, bwd_right),
        )
        self.map = mp
        self.end = None
        self.x_bounds = None
        self.y_bounds = None
        # self.collision_checking_time = 0

    def _goal(
        self,
        pos: "Position"
    ) -> bool:
        if self.x_bounds[0] <= pos.x <= self.x_bounds[1] and \
           self.y_bounds[0] <= pos.y <= self.y_bounds[1] and \
           abs(self.end.theta - pos.theta) % (2*pi) <= MAX_THETA_ERR:
            return True
        return False


    def _expand(
        self,
        node: "Node", 
    ):
        st = node.c_pos

        for v, s, d, mv, f in self.moves:
            nxt_pos = f(st)
            nxt_pos_tup = nxt_pos.snap().to_tuple()
            
            # collision_checking_start_time = time.time()
            if nxt_pos_tup in self.closed or has_collision(st, mv, self.map):
                # self.collision_checking_time += time.time() - collision_checking_start_time
                continue
            # self.collision_checking_time += time.time() - collision_checking_start_time

            penalty = 0
            if v != node.v or s != node.s:
                penalty = PENALTY_STOP

            nxt_node = Node(nxt_pos.snap(), nxt_pos, node.g + penalty + d, euclidean(nxt_pos, self.end), node, v, s, d)            

            # there is a shorter way to reach a node that is already in open set
            if self.open_h.get(nxt_pos_tup, -1) > nxt_node.f:
                for i, br in enumerate(self.open):
                    if br == nxt_node:
                        # replace br with cell
                        br.f = -1
                        heapq._siftdown(self.open, 0, i)
                        heapq.heappop(self.open)
                        break

            heapq.heappush(self.open, nxt_node)
            self.open_h[nxt_pos_tup] = nxt_node.f

    
    def _set_bounds(self):
        vv = calc_vector(self.end.theta, 1)
        vh = calc_vector(self.end.theta - pi/2, 1)

        end = np.array([self.end.x, self.end.y])
        _TR = end + vh * MAX_X_ERR[1] + vv * MAX_Y_ERR[0]
        _BL = end - vh * MAX_X_ERR[0] - vv * MAX_Y_ERR[1]
        
        self.x_bounds = sorted([_TR[0], _BL[0]])
        self.y_bounds = sorted([_TR[1], _BL[1]])

        # Ensure that the range of the x_bounds and y_bounds are within the MAP DIMENSIONS [0, 200]
        self.x_bounds = [max(0, self.x_bounds[0]), min(self.x_bounds[1], MAP_WIDTH)]
        self.y_bounds = [max(0, self.y_bounds[0]), min(self.y_bounds[1], MAP_HEIGHT)]

    def search(
        self,
        st: "Position",
        end: "Position",
    ) -> List["Node"]:
        start_time = time.time()
        # self.collision_checking_time = 0
        logger.info(f'Start search from {st} to {end}')
        end_node = Node(end, end, 0, 0)
        self.end = end
        self.open = [Node(st.snap(), st, 0, 0)]
        self.open_h = {} # keep track of unique cells that are in open set
        self.closed = []
        self._set_bounds()

        while self.open:

            node = heapq.heappop(self.open)
            tup = node.pos.to_tuple()
            logger.debug(f'{node} {node.parent}')

            if self._goal(node.c_pos):
                logger.info(f'Found goal {end_node}')
                # print("Astar Search Runtime:", time.time() - start_time, "s")
                # print("Astar Collision Checking Runtime:", self.collision_checking_time, "s")
                # print()
                return self._reconstruct(node) # AlgoOutput -> An array of `Node` from start to goal/end

            self.closed.append(tup)
            self._expand(node)

            for o in self.open[:5]:
                logger.debug(f'{o.c_pos}, {o}')

        logger.info(f'Unable to reach {end} from {st}')
        return []


    def _reconstruct(
        self,
        last: "Node"
    ) -> List["Node"]:
        '''Reconstructs the shortest path taken to reach the goal

        Returns:
            An array of `Node` from start to goal/end'''
        res = []

        while last:
            res.append(last)
            last = last.parent

        return res[::-1]