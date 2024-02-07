from math import cos, sin
import numpy as np
from typing import List, Tuple

from arena.obstacle import Obstacle
from common.enums import Direction
from common.types import Position
from common.consts import OBSTACLE_WIDTH

_mappings = {
    '1': Direction.NORTH,
    '2': Direction.SOUTH,
    '3': Direction.EAST,
    '4': Direction.WEST
}

def calc_vector(
    theta: float,
    length: float
) -> np.array:
    """Calculate a vector of specified length, pointing in direction theta radians

    Args:
        theta (float) : Direction of vector
        length (float) : Magnitude of vector
    
    Returns:
        np.array : Column vector. Typically to calculate the vector going from robot's bottom left to top left corner.
    """
    return np.array([
        cos(theta) * length,
        sin(theta) * length
    ])


def rotate_vector(
    v: np.array,
    theta: float
) -> np.array:
    return np.array([v[0]*cos(theta) - v[1]*sin(theta), v[0]*sin(theta) + v[1]*cos(theta)])


def euclidean(
    st: Position,
    end: Position
) ->  float:
    return ((st.y - end.y)**2 + (st.x - end.x)**2)**.5

def evaluate_parametric(
    center_x: float,
    center_y: float,
    radius_x: float,
    radius_y: float,
    rotation: float,
    angle: float
) -> list:
    
    '''
    Given an angle, return the point lying on the ellipse that is at t
    radians counterclockwise from the point(x_radius, 0), or its rotated image if
    this ellipse is rotated at angle rotation
    '''
    x = center_x + radius_x * cos(angle) * cos(rotation) - radius_y * sin(angle) * sin(rotation)
    y = center_y + radius_x * cos(angle) * sin(rotation) + radius_y * sin(angle) * cos(rotation)
    return [x, y]


def parse_map_str(s: str) -> Tuple[List[int], List["Obstacle"]]:
    obs = list(map(lambda x:x.split(','), s.split('|')))
    return [int(o[0]) for o in obs], [Obstacle(int(o[1])*10, int(o[2])*10, _mappings[o[3]]) for o in obs]