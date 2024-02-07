from math import pi

from arena.map import Map
from arena.obstacle import Obstacle
from common.enums import Direction, Movement
from common.types import Position


def test_fw():
    obs = [
        Obstacle(50, 50, Direction.NORTH),
        Obstacle(100, 50, Direction.NORTH),
        Obstacle(50, 100, Direction.NORTH),
        Obstacle(100, 100, Direction.NORTH)
    ]
    mp = Map(obs)

    origin = Position(40, 20, pi/2)
    restricted = mp.priority_obs(origin, Movement.FWD)

    assert len(restricted) == 1
    assert restricted[0] == obs[0]


def test_fl():
    obs = [
        Obstacle(80, 40, Direction.WEST),
        Obstacle(120, 20, Direction.WEST),
        Obstacle(120, 40, Direction.NORTH),
        Obstacle(10, 70, Direction.SOUTH),
        Obstacle(10, 150, Direction.SOUTH),
        Obstacle(100, 130, Direction.WEST),
        Obstacle(110, 130, Direction.SOUTH),
        Obstacle(160, 30, Direction.NORTH)
    ]
    mp = Map(obs)

    origin = Position(76.8, 36, 0)
    restricted = mp.priority_obs(origin, Movement.FWD_LEFT)

    assert len(restricted) == 3
    assert restricted == obs[:3]


def test_fl_2():
    obs = [
        Obstacle(150, 90, Direction.NORTH),
        Obstacle(70, 80, Direction.NORTH),
        Obstacle(50, 150, Direction.EAST),
        Obstacle(30, 80, Direction.SOUTH),
        Obstacle(120, 30, Direction.EAST),
        Obstacle(90, 110, Direction.WEST),
        Obstacle(180, 180, Direction.SOUTH),
        Obstacle(20, 80, Direction.NORTH)
    ]
    mp = Map(obs)


    origin = Position(110.8, 68, 0)
    restricted = mp.priority_obs(origin, Movement.FWD_LEFT)

    assert len(restricted) == 1
    assert restricted[0] == obs[0]
    
    
def test_fr():
    obs = [
        Obstacle(70, 80, Direction.NORTH),
        Obstacle(90, 110, Direction.WEST),
        Obstacle(50, 150, Direction.EAST),
        Obstacle(30, 80, Direction.SOUTH),
        Obstacle(120, 30, Direction.EAST),
        Obstacle(150, 90, Direction.NORTH),
        Obstacle(180, 180, Direction.SOUTH),
        Obstacle(20, 80, Direction.NORTH)
    ]
    mp = Map(obs)

    origin = Position(40.8, 49, pi/2)
    restricted = mp.priority_obs(origin, Movement.FWD_RIGHT)

    assert len(restricted) == 2
    assert obs[0] in restricted and obs[1] in restricted


def test_br():
    obs = [
        Obstacle(180, 160, Direction.SOUTH)
    ]
    mp = Map(obs)

    origin = Position(155.2, 105.8, pi)
    restricted = mp.priority_obs(origin, Movement.BWD_RIGHT)

    assert len(restricted) == 1
    assert restricted[0] == obs[0]

    