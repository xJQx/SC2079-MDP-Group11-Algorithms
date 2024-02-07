from tkinter import Canvas

from common.consts import SCALED_MAP_HEIGHT, TK_SCALE
from common.enums import Path
from path_finding.dubins_path import PathParams


def draw_dubins(
    canvas: Canvas,
    path: PathParams
):
    # tangent
    canvas.create_line(
        TK_SCALE*path.pt1[0], 
        SCALED_MAP_HEIGHT-TK_SCALE*path.pt1[1], 
        TK_SCALE*path.pt2[0],
        SCALED_MAP_HEIGHT-TK_SCALE*path.pt2[1]    
    )