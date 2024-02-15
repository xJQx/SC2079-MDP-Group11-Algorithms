from math import pi
import numpy as np

from arena.map import Map
from common.consts import (
    WPS_BL,
    WPS_BR,
    WPS_FL,
    WPS_FR,
    DIST_FW
)
from common.enums import Movement
from common.types import Position
from common.utils import calc_vector

def has_collision(
    st: Position,
    movement: Movement,
    mp: Map
) -> bool:

    obs = mp.priority_obs(st, movement)

    if movement == Movement.FWD_LEFT:
        wps = WPS_FL
    elif movement == Movement.BWD_LEFT:
        wps = WPS_BL
    elif movement == Movement.FWD_RIGHT:
        wps = WPS_FR
    elif movement == Movement.BWD_RIGHT:
        wps = WPS_BR
    else:
        # fwd or bwd
        v = calc_vector(st.theta, DIST_FW)
        new = st.clone()
        if movement == Movement.BWD:
            v *= -1
        new.add(v)
        return not mp.is_valid(new, obs)
    
    v_st = np.array([st.x, st.y])
    v_u = calc_vector(st.theta - pi/2, 1)
    v_r = calc_vector(st.theta, 1)
    
    for wp in wps:
        pos = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), (st.theta + wp[2]) % (2*pi))
        if not mp.is_valid(pos, obs):
            return True
    return False
