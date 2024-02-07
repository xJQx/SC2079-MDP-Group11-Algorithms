from tkinter import Canvas

from arena.obstacle import Obstacle
from common.consts import (
    SCALED_MAP_HEIGHT,
    SCALED_OBSTACLE_WIDTH, 
    TK_SCALE,
    IMG_THICKNESS
)
from common.enums import Direction


def draw_obstacle(
    canvas: Canvas, 
    obs: Obstacle
):   
    """Draw an obstacle object on a canvas

    Args:
        canvas (tkinter.Canvas) Canvas object
        x (float) : x-coord of obstacle's bottom left corner
        y (float) : y-coord of obstacle's bottom left corner
        facing (float) : facing of image on obstacle
    """
    y = SCALED_MAP_HEIGHT - TK_SCALE * obs.y
    x = TK_SCALE * obs.x
    img_x = x
    img_y = y
    if obs.facing == Direction.NORTH:
        img_y -= SCALED_OBSTACLE_WIDTH - IMG_THICKNESS
        img_height = IMG_THICKNESS
        img_width = SCALED_OBSTACLE_WIDTH
    elif obs.facing == Direction.SOUTH:
        img_height = IMG_THICKNESS
        img_width = SCALED_OBSTACLE_WIDTH
    elif obs.facing == Direction.WEST:
        img_height = SCALED_OBSTACLE_WIDTH
        img_width = IMG_THICKNESS
    else:
        img_x += SCALED_OBSTACLE_WIDTH - IMG_THICKNESS
        img_height = SCALED_OBSTACLE_WIDTH
        img_width = IMG_THICKNESS

    # obstacle
    canvas.create_rectangle(
        x, 
        y, 
        x + SCALED_OBSTACLE_WIDTH, 
        y - SCALED_OBSTACLE_WIDTH, 
        fill = 'red'
    )
    
    # image
    canvas.create_rectangle(
        img_x, 
        img_y,
        img_x + img_width, 
        img_y - img_height,
        fill = 'darkred'
    )