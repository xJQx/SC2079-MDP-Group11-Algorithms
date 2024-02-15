from math import pi
import numpy as np
from arena.map import Map, Obstacle

from common.consts import (
    DIST_FW,
    DIST_BW,
    WPS_BL,
    WPS_BR,
    WPS_FL,
    WPS_FR,
    OBSTACLE_WIDTH,
    ROBOT_WIDTH,
    ROBOT_HEIGHT
) 
from common.enums import Movement, Direction
from common.types import Position
from path_finding.path_validation import has_collision
from path_finding.astar import Node
from simulator import Simulator
from robot.move import *

def test_forward_check_detected(collision_mp_2):
    st = Position(0, 0, pi/2)
    cehck = []
    check = has_collision(st, Movement.FWD_LEFT, collision_mp_2)
    assert check == True