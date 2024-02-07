from math import pi

from common.consts import (
    OBSTACLE_WIDTH,
    ROBOT_MIN_CAMERA_DIST,
    ROBOT_HEIGHT,
    ROBOT_WIDTH
)
from common.enums import Direction
from common.types import Position


class Obstacle:
    def __init__(
        self,
        x: float,
        y: float,
        facing: Direction
    ):
        self.x = x
        self.y = y
        self.facing = facing
        self.middle = (x+OBSTACLE_WIDTH/2, y+OBSTACLE_WIDTH/2)

    
    def to_pos(self) -> Position:
        x = self.x
        y = self.y
        theta = None

        pad = (ROBOT_WIDTH - OBSTACLE_WIDTH) / 2

        if self.facing == Direction.NORTH:
            y += ROBOT_MIN_CAMERA_DIST + OBSTACLE_WIDTH + ROBOT_HEIGHT
            x += pad + OBSTACLE_WIDTH
            theta = -pi/2
        elif self.facing == Direction.SOUTH:
            y -= ROBOT_MIN_CAMERA_DIST + ROBOT_HEIGHT
            x -= pad
            theta = pi/2
        elif self.facing == Direction.EAST:
            y -= pad
            x += ROBOT_MIN_CAMERA_DIST + OBSTACLE_WIDTH + ROBOT_WIDTH
            theta = pi
        elif self.facing == Direction.WEST:
            y += pad + OBSTACLE_WIDTH
            x -= ROBOT_MIN_CAMERA_DIST + ROBOT_WIDTH
            theta = 0

        return Position(x, y, theta)