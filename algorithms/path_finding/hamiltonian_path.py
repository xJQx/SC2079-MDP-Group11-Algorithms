import heapq
import logging
import multiprocessing as mp
import time
from typing import List
import math
from enum import Enum

from arena.map import Map
from common.types import Position
from common.utils import euclidean
from path_finding.astar import AStar, Node


MAX_ASTAR_F_COST = 99999

logger = logging.getLogger('HAMILTONIAN PATH')

# `knn()` -> Not Used
def knn(mp: "Map", src: "Position") -> List[List["Node"]]:
    astar = AStar(mp)
    path = [src] + [o.to_pos() for o in mp.obstacles]

    for i in range(1, len(path)):
        mn = float('inf')
        mn_i = i+1

        for j in range(i, len(path)):
            dist = euclidean(path[i-1], path[j])
            if dist < mn:
                mn = dist
                mn_i = j

        path[mn_i], path[i] = path[i], path[mn_i]

    res = []
    prev = src
    for i in range(1, len(path)):
        res.append(astar.search(prev, path[i]))
        prev = res[-1][-1].c_pos
    return res


def _permutate(n: int, start_from_zero: bool) -> List[List[int]]:
    """
    This function generates all permutations of numbers from 0 to n-1 and returns them as a list of lists. 
    If `start_from_zero` is True, it filters the permutations to include only those where 0 is the first element.

    Example:
        If n = 4, the function will return the permutations of [[0, 1, 2, 3]] or [[1, 2, 3, 0]] depending on the value of start_from_zero.

    """
    res = []

    def helper(curr: List[int]):
        if len(curr) == n:
            res.append(curr)
            return
        for i in range(n):
            if i not in curr:
                helper([*curr, i])
    helper([])
    if start_from_zero:
        res = list(filter(lambda p:p[0] == 0, res))
    return res


class AlgoType(Enum):
    """Enumeration for possible algorithms to be used for `HamiltonianSearch`"""
    EXHAUSTIVE_ASTAR = "Exhaustive Astar"
    EUCLIDEAN = "Euclidean"
    BFS = "Breadth First Search"

class SearchProcess(mp.Process):
    """A Process (similar to a Thread) used for multiprocessing to speed up algorithm computation time"""
    def __init__(
        self,
        pos: List["Position"],
        astar: AStar,
        todo: mp.Queue,
        done: mp.Queue,
        i:int,
        algo_type = AlgoType
    ):
        super().__init__()
        self.astar = astar
        self.pos = pos
        self.todo = todo
        self.done = done
        self.i = i
        self.algo_type = algo_type
        logger.info(f'Spawning P{i}')


    def _search(
        self,
        st: int,
        end: int
    ) -> float:
        """Search According to the `AlgoType`
        @returns:
            Exhaustive Astar: Astar 'f' cost
            Euclidean: Euclidean Distance
            BST: BST cost ('g' cost)
        """
        logger.info(f'P{self.i} start search {st, end}')

        match (self.algo_type):
            case AlgoType.EXHAUSTIVE_ASTAR:
                # Returns astar 'f' cost
                path = self.astar.search(self.pos[st], self.pos[end])
                return path[-1].f if path else MAX_ASTAR_F_COST
            case AlgoType.EUCLIDEAN:
                # Return Euclidean Distance
                start_pos = self.pos[st]
                end_pos = self.pos[end]
                euclidean_distance = math.sqrt((end_pos.x - start_pos.x) ** 2 + (end_pos.y - start_pos.y) ** 2)
                return euclidean_distance
            case AlgoType.BFS:
                # TODO: BFS
                raise NotImplementedError()
            case _:
                raise Exception("Invalid AlgoType")
    
    def run(self):
        while 1:
            try:
                st, end = self.todo.get()
                self.done.put((st, end, self._search(st, end)))
            except:
                logger.info(f'P{self.i} finished')
                return

class HamiltonianSearch:
    """
    Uses `Astar` (If AlgoType.EXHAUSIVE_ASTAR) to do an exhaustive search on all possible permutations of order of obstacles to visit 
    and finds the lowest cost permutation and its associated paths.

    Uses Multiprocessing (parameter `n` which defaults to 8) to lower computation time.

    Params:

        `map`: Map object
        `src`: Position object of the source/starting position
        `n` = 8: Number of child processes to run concurrently

    Main Method: `search()`
        
        Returns:
            min_perm`: lowest cost order of visiting all the obstacles starting from starting location;
            `loc_mn_path`: An array of a path Array of `Node` where each inner path Array is the path from one location to another;
    """

    def __init__(
        self,
        map: "Map", 
        src: "Position",
        algo_type: AlgoType,
        n: int = 8
    ):
        self.astar = AStar(map)
        self.src = src
        self.pos = [src] + [o.to_pos() for o in map.obstacles]
        self.n = n
        self.algo_type = algo_type

        # TODO: BFS
        if algo_type == AlgoType.BFS:
            raise NotImplementedError()

    
    def search(self, top_n: int = 3):
        print("----- Start Hamiltonian Search -----")

        st = time.time()
        n = len(self.pos)
        m = int(n*n - n - (n-1)) # total paths to calc from pt to pt (excluding from pt_a to pt_a and from pt_a to 0)
        perms = _permutate(n, True)
        edges = [[0 for _ in range(n)] for _ in range(n)]
        todo = mp.Queue() # (r, c)
        done = mp.Queue() # (r, c, astar f cost)

        for r in range(n):
            for c in range(n):
                if r != c and c != 0:
                    todo.put((r, c))

        # Create multiple Threads/Process and starts them
        for i in range(self.n):
            p = SearchProcess(self.pos, self.astar, todo, done, i, self.algo_type)
            p.daemon = True
            p.start()

        while m:
            r, c, f = done.get()
            edges[r][c] = f
            logger.info(f'{r} -> {c} ({f})')
            m -= 1
        logger.info(f'Adj list completed in {time.time()-st} s')
        print(f'Adj list completed in {time.time()-st} s')

        # get shortest path, i.e., lowest cost among all permutations
        st2 = time.time()
        h = []
        for i, perm in enumerate(perms):
            cost = sum([edges[perm[i]][perm[i+1]] for i in range(n-1)])
            heapq.heappush(h, (cost, perm))

        loc_mn_path = []
        loc_mn_f = float('inf')
        min_perm = []
        for _ in range(min(top_n, len(h))):

            path = []
            prev = self.pos[0]
            cost, perm = heapq.heappop(h)
            f = 0
            logger.info(f'Calculating path for {perm}')

            for i in range(1, n):
                segment = self.astar.search(prev, self.pos[perm[i]])

                if segment:
                    path.append(segment)
                    prev = segment[-1].c_pos
                    f += segment[-1].f
                else:
                    f += MAX_ASTAR_F_COST

                if f > loc_mn_f:
                    break

            if f < loc_mn_f:
                loc_mn_f = f
                loc_mn_path = path
                min_perm = perm
            if f < MAX_ASTAR_F_COST:
                print("f < MAX_ASTAR_F_COST")
                print(f'Time (pathfinding) {time.time()-st2} s')
                print(f'Total runtime {time.time()-st} s')
                return perm, path
        
        print(f'Time (pathfinding) {time.time()-st2} s')
        print(f'Total runtime {time.time()-st} s')
        return min_perm, loc_mn_path # AlgoOutput -> `min_perm`: lowest cost order of visiting all the obstacles starting from starting location; `loc_mn_path`: An array of a path Array of `Node` where each inner path Array is the path from one location to another