from math import pi

from arena.map import Map
from arena.obstacle import Obstacle
from common.enums import Direction
from common.types import Position
from path_finding.hybrid_astar import Node
from path_finding.dubins_path import DubinsPath
from simulator import Simulator
from simulator.components.dubins import draw_dubins


def test_BR_TL():
    st_pos = Position(150, 30, pi/2)
    st_node = Node(st_pos, st_pos, 0, 0)
    obs = Obstacle(50, 40, Direction.NORTH)
    end_pos = obs.to_pos()

    mp = Map([obs])
    dubins = DubinsPath()

    sim = Simulator(mp)
    sim.path = [st_node]
    canvas = sim.canvas

    for path in dubins._find_paths(st_pos, end_pos):
        draw_dubins(canvas, path)
    sim.run()


def test_TL_BR():
    st_pos = Position(40, 130, pi/2)
    st_node = Node(st_pos, st_pos, 0, 0)
    obs = Obstacle(150, 40, Direction.NORTH)
    end_pos = obs.to_pos()

    mp = Map([obs])
    dubins = DubinsPath()

    sim = Simulator(mp)
    sim.path = [st_node]
    canvas = sim.canvas

    for path in dubins._find_paths(st_pos, end_pos):
        draw_dubins(canvas, path)
    sim.run()


def test_LTR():
    st_pos = Position(50, 60, pi/2)
    st_node = Node(st_pos, st_pos, 0, 0)
    obs = Obstacle(110, 60, Direction.EAST)
    end_pos = obs.to_pos()

    mp = Map([obs])
    dubins = DubinsPath()

    sim = Simulator(mp)
    sim.path = [st_node]
    canvas = sim.canvas
    
    for path in dubins._find_paths(st_pos, end_pos):
        draw_dubins(canvas, path)
    sim.run()
