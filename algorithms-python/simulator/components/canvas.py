import tkinter as tk
from tkinter import Tk, Canvas

from common.consts import (
    GRID_WIDTH,
    SCALED_MAP_HEIGHT,
    SCALED_MAP_WIDTH
)


def draw_canvas(window: Tk) -> Canvas:
    """Create a canvas object
    
    Args:
        window (tk.Tk) : Window object to add canvas to
    
    Returns:
        Canvas : Created canvas object
    """
    canvas = tk.Canvas(
        window, 
        bg='white', 
        width=SCALED_MAP_WIDTH, 
        height=SCALED_MAP_HEIGHT
    )
    canvas.pack()

    # grid lines
    for c in range(GRID_WIDTH, SCALED_MAP_WIDTH, GRID_WIDTH):
        canvas.create_line((c, 0, c, SCALED_MAP_HEIGHT), fill='gray' if c % (GRID_WIDTH * 2) == 0 else 'lightgray')

    for r in range(GRID_WIDTH, SCALED_MAP_HEIGHT, GRID_WIDTH):
        canvas.create_line((0, r, SCALED_MAP_WIDTH, r), fill='gray' if r % (GRID_WIDTH * 2) == 0 else 'lightgray')
    
    return canvas