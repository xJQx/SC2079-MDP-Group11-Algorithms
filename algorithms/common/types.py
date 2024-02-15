from math import pi
import numpy as np
from typing import Tuple

from common.consts import (
    SNAP_COORD,
    SNAP_THETA
)

class Position:

    def __init__(
        self,
        x: float,
        y: float,
        theta: float
    ):
        self.x = x
        self.y = y
        self.theta = theta


    def snap(
        self,
    ) -> "Position":
        x = int(round(self.x / SNAP_COORD) * SNAP_COORD)
        y = int(round(self.y / SNAP_COORD) * SNAP_COORD)
        theta = round(self.theta % (2*pi) / pi * 180 / SNAP_THETA) * SNAP_THETA / 180 * pi

        return Position(x, y, theta)
    

    def clone(self) -> "Position":
       return Position(self.x, self.y, self.theta)
       

    def add(
        self, 
        vec: np.array
    ):
        self.x += vec[0]
        self.y += vec[1]


    def to_np(self) -> np.array:
        return np.array([self.x, self.y])
    

    def to_tuple(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.theta


    def __str__(self) -> str:
        return f'(x:{self.x:6.2f}, y:{self.y:6.2f}, θ:{self.theta:6.2f})'