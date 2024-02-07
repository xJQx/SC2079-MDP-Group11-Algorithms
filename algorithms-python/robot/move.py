from math import pi
from common.consts import (
    DIST_BL,
    DIST_BR,
    DIST_BW,
    DIST_FL,
    DIST_FR,
    DIST_FW
)
from common.utils import calc_vector
from common.types import Position


D_THETA = pi/2


def fwd(pos: "Position") -> "Position":
    new = pos.clone()
    new.add(calc_vector(pos.theta, DIST_FW))
    return new


def bwd(pos: "Position") -> "Position":
    new = pos.clone()
    new.add(calc_vector(pos.theta, -DIST_BW))
    return new


def fwd_left(pos: "Position") -> "Position":
    vh = calc_vector(pos.theta-pi/2, DIST_FL[0])
    vv = calc_vector(pos.theta, DIST_FL[1])
    new = pos.clone()
    new.add(vv + vh)
    new.theta = pos.theta + pi/2
    return new


def fwd_right(pos: "Position") -> "Position":
    vh = calc_vector(pos.theta-pi/2, DIST_FR[0])
    vv = calc_vector(pos.theta, DIST_FR[1])
    new = pos.clone()
    new.add(vv + vh)
    new.theta = pos.theta - pi/2
    return new


def bwd_left(pos: "Position") -> "Position":
    vh = calc_vector(pos.theta-pi/2, DIST_BL[0])
    vv = calc_vector(pos.theta, DIST_BL[1])
    new = pos.clone()
    new.add(vv + vh)
    new.theta = pos.theta - pi/2
    return new


def bwd_right(pos: "Position") -> "Position":
    vh = calc_vector(pos.theta-pi/2, DIST_BR[0])
    vv = calc_vector(pos.theta, DIST_BR[1])
    new = pos.clone()
    new.add(vv + vh)
    new.theta = pos.theta + pi/2
    return new