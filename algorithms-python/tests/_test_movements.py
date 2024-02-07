from math import pi

from common.consts import (
    DIST_BR, 
    DIST_BL, 
    DIST_BW, 
    DIST_FL,
    DIST_FR, 
    DIST_FW
)
from common.types import Position
from robot.move import *


def test_move_fwd(src):
    src = Position(*src)
    dst = fwd(src)

    assert dst.x == src.x
    assert dst.y == src.y + DIST_FW
    assert dst.theta == src.theta


def test_move_bwd(src):
    src = Position(*src)
    dst = bwd(src)

    assert dst.x == src.x
    assert dst.y == src.y - DIST_BW
    assert round(dst.theta, 2) == 1.57


def test_move_fwd_left(src):
    src = Position(*src)
    dst = fwd_left(src)

    assert round(dst.x, 2) == round(src.x + DIST_FL[0], 2)
    assert round(dst.y, 2) == round(src.y + DIST_FL[1], 2)
    assert dst.theta == pi


def test_move_fwd_right(src):
    src = Position(*src)
    dst = fwd_right(src)

    assert round(dst.x, 2) == round(src.x + DIST_FR[0], 2)
    assert round(dst.y, 2) == round(src.y + DIST_FR[1], 2)
    assert round(dst.theta, 2) == 0


def test_move_bwd_left(src):
    src = Position(*src)
    dst = bwd_left(src)
    
    assert round(dst.x, 2) == round(src.x + DIST_BL[0], 2)
    assert round(dst.y, 2) == round(src.y + DIST_BL[1], 2)
    assert round(dst.theta, 2) == 0


def test_move_bwd_right(src):
    src = Position(*src)
    dst = bwd_right(src)

    assert round(dst.x, 2) == round(src.x + DIST_BR[0], 2)
    assert round(dst.y, 2) == round(src.y + DIST_BR[1], 2)
    assert dst.theta == pi