import logging
import heapq
from typing import List, Optional

from arena.map import Map
from common.consts import (
    PENALTY_STOP,
    ROBOT_TIME_STEP
)
from common.enums import Movement
from common.types import Position
from common.utils import euclidean
from robot.move import (
    bwd,
    bwd_left,
    bwd_right,
    fwd,
    fwd_left,
    fwd_right
)
from path_finding.path_validation import has_collision


logger = logging.getLogger('HYBRID A*')


class Node:

    def __init__(
        self,
        pos: Position,
        c_pos: Position,
        g: float,
        h: float,
        parent: Optional["Node"] = None,
        v: Optional[int] = 1,
        s: Optional[int] = 0
    ):
        self.pos = pos
        self.c_pos = c_pos # pos in continuous scale
        self.g = g # st to curr
        self.h = h # curr to end
        self.f = g + h # total

        self.v = v # prev motion's vert direction, -1: bwd, 1: fwd
        self.s = s # prev motion's steering direction, -1: left, 0: straight, 1: fwd

        self.parent = parent
    

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
        return f'Node(x:{self.pos.x:6.2f}, y:{self.pos.y:6.2f}, θ:{self.pos.theta:6.2f}, g:{self.g:6.2f}, h:{self.h:6.2f}, f:{self.f:6.2f})'


movements = {
    (1, -1): Movement.FWD_LEFT,
    (1, 0): Movement.FWD,
    (1, 1): Movement.FWD_RIGHT,
    (-1, -1): Movement.BWD_LEFT,
    (-1, 0): Movement.BWD,
    (-1, 1): Movement.BWD_RIGHT
}


class HybridAStar:

    def __init__(
        self,
        map: "Map"
    ):
        self.map = map
        self.st = None
        self.end = None

        self.open = []
        self.open_h = {}

        # fwd/bwd, left/straight/right, func 
        self.comb = (( 1, -1, fwd_left), ( 1, 0, fwd), ( 1, 1, fwd_right), 
                     (-1, -1, bwd_left), (-1, 0, bwd), (-1, 1, bwd_right))


    def _expand(
        self,
        node: "Node"
    ):
        p_pos = node.c_pos # parent pos

        for v, s, f in self.comb:
            # don't undo prev move
            if node.v * v == -1 and node.s == s:
                continue

            c_pos = f(p_pos) # continuous pos

            if not self.map.is_valid(c_pos):
                continue

            # if has_collision(node.c_pos, ROBOT_TIME_STEP, movements[(v, s)], self.map):
            #     continue

            g = ROBOT_TIME_STEP * (PENALTY_STOP if (v != node.v or s != node.s) else 1)
            h = euclidean(self.end.pos, p_pos)
            s_pos = c_pos.snap() # snapped pos
            s_pos_tup = s_pos.to_tuple()
            cell = Node(s_pos, c_pos, node.g + g, h, node, v, s)

            if self.open_h.get(s_pos_tup, -1) > cell.f:
                for i, br in enumerate(self.open):
                    if br == cell:
                        # replace br with cell
                        br.f = -1
                        heapq._siftdown(self.open, 0, i)
                        heapq.heappop(self.open)
                        break

            heapq.heappush(self.open, cell)
            self.open_h[s_pos_tup] = cell.f


    def _reconstruct(
        self,
        last: "Node"
    ) -> List["Node"]:
        res = []

        while last:
            res.append(last)
            last = last.parent

        return res[::-1]
    

    def search(
        self,
        st: Position,
        end: Position
    ) -> List["Node"]:
        
        self.st = Node(st.snap(), st, 0, 0)
        self.end = Node(end.snap(), end, 0, 0)
        self.open = [self.st]
        self.open_h = {}
        self.open_h[st.snap().to_tuple()] = 0
        self.closed = set()
        
        logger.debug(f'Start search from {st} to {end}')

        while self.open:
            curr = heapq.heappop(self.open)
            curr_tup = curr.pos.to_tuple()

            if curr_tup in self.closed:
                continue

            self.closed.add(curr_tup)
            self.open_h.pop(curr_tup)

            # reached destination
            if curr == self.end:
                logger.debug(f'Found goal {end}')
                return self._reconstruct(curr)
            
            self._expand(curr)

        logger.debug(f'Unable to reach {end} from {st}')
        return []