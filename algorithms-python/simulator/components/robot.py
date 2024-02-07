from math import pi
import numpy as np
from tkinter import Canvas
from typing import Tuple

from common.consts import (
    ROBOT_BTM_LEFT_CIRCLE_RAD,
    SCALED_MAP_HEIGHT,
    SCALED_ROBOT_HEIGHT,
    SCALED_ROBOT_WIDTH,
    SCALED_ROBOT_TURNING_RADIUS
)
from common.utils import calc_vector


def draw_robot(
    canvas: Canvas, 
    x: float, 
    y: float, 
    theta: float,
    **kwargs
) -> Tuple[int, int, int]:
    """Draw a robot object on a canvas

    Args:
        canvas (tkinter.Canvas) Canvas object
        x (float) : x-coord of robot's bottom left corner
        y (float) : y-coord of robot's bottom left corner
        theta (float) : facing of robot
        **kwargs : Arbitrary tkinter _create() args for robot body

    Returns:
        Tuple[int, int] : Object ID of robot body and robot origin, so that they can be cleaned up after each update
    """
    y = SCALED_MAP_HEIGHT - y
    origin = np.array([x, y])

    vector_up = calc_vector(-theta, SCALED_ROBOT_HEIGHT)
    vector_right = calc_vector(-theta+pi/2, SCALED_ROBOT_WIDTH) #np.array([-vector_up[1], vector_up[0]])

    # robot body
    robot_body = canvas.create_polygon(
        (
            x, y, # btm left
            *(origin + vector_up), # top left 
            *(origin + vector_up + vector_right), # top right 
            *(origin + vector_right), # btm right
        ),
        fill='',
        width=1,
        **kwargs
    )
    # indicates btm left point of robot
    robot_btm_left = canvas.create_oval(
        (
            x-ROBOT_BTM_LEFT_CIRCLE_RAD,
            y-ROBOT_BTM_LEFT_CIRCLE_RAD,
            x+ROBOT_BTM_LEFT_CIRCLE_RAD,
            y+ROBOT_BTM_LEFT_CIRCLE_RAD
        ), 
        fill='red',
        width=1
    )

    # turning arcs
    v_ts_norm = calc_vector(-theta, SCALED_ROBOT_TURNING_RADIUS)
    v_norm = calc_vector(-pi/2, SCALED_ROBOT_TURNING_RADIUS)
    
    return robot_body, robot_btm_left