from enum import Enum


class Direction(Enum):
    """Enumeration object for obstacle's image facings"""
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


class Movement(Enum):
    """Enumeration for robot's 6 possible movement directions"""
    FWD = 1
    BWD = 2
    FWD_LEFT = 3
    FWD_RIGHT = 4
    BWD_LEFT = 5
    BWD_RIGHT = 6


class TurnDirection(Enum):
    """Clockwise or anticlockwise"""
    CLOCKWISE = 0
    ANTICLOCKWISE = 1


class Path(Enum):
    """Dubins path type"""
    LSL = 1
    LSR = 2
    RSL = 3
    RSR = 4
    LRL = 5
    RLR = 6