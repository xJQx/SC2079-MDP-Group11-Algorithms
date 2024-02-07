import logging
from math import pi
import numpy as np
from typing import List
import tkinter as tk

from arena.map import Map
from arena.obstacle import Obstacle
from common.consts import (
    SCALED_MAP_HEIGHT,
    SCALED_MAP_WIDTH,
    SCALED_OBSTACLE_WIDTH,
    SCALED_ROBOT_MIN_CAMERA_DIST,
    SCALED_ROBOT_WIDTH,
    TK_SCALE,
    WPS_BL,
    WPS_BR,
    WPS_FL,
    WPS_FR
)
from common.enums import Direction
from common.types import Position
from common.utils import calc_vector
from path_finding.astar import Node
from simulator.components.canvas import draw_canvas
from simulator.components.obstacle import draw_obstacle
from simulator.components.robot import draw_robot


logger = logging.getLogger('MAP')


class Simulator:
    """The Map class displays the obstacles and robot's location at every timestep on a canvas. 
    Traverse the waypoints in discrete timesteps by pressing <Enter> key.

    Attributes:
        window (tkinter.Tk) : Window object
        canvas (tkinter.Canvas) : Canvas object
        path (List[Tuple[float, float, float]]) : List of waypoints that the robot will traverse
        obstacles (List[Tuple[float, float, Direction]]) : List of obstacles
        prev_state (List[int]) : List of canvas object IDs of the robot component, to be deleted at the end of each timestep
    """
    def __init__(self, mp: Map):
        self.window = tk.Tk()
        self.window.geometry(f'{SCALED_MAP_WIDTH}x{SCALED_MAP_HEIGHT}')
        self.window.title('Map')
        self.window.bind('<Return>', lambda e: self._display_timestep(1))
        self.window.bind('<Right>', lambda e:self._display_timestep(1))
        self.window.bind('<Left>', lambda e:self._display_timestep(-1))

        self.canvas = draw_canvas(self.window)
        self.path = []
        self.obstacles = []
        self.prev_state = []
        self.t = -1

        self.map = mp
        self._set_obstacles(mp.obstacles)


    def _set_obstacles(
        self,
        obstacles: List[Obstacle]
    ):
        """Set a list of obstacles for the map and display them as canvas objects

        Args:
            obstacles (List[Obstacle]]) : List of obstacles
        """
        robot_pad = (SCALED_ROBOT_WIDTH - SCALED_OBSTACLE_WIDTH) / 2
        for obs in obstacles:
            draw_obstacle(
                self.canvas, 
                obs
            )

            # draw desired final destinations
            ghost_x = obs.x * TK_SCALE
            ghost_y = obs.y * TK_SCALE
            ghost_theta = 0
            if obs.facing == Direction.NORTH:
                ghost_x += SCALED_OBSTACLE_WIDTH + \
                           robot_pad
                ghost_y += SCALED_OBSTACLE_WIDTH + \
                           SCALED_ROBOT_WIDTH + \
                           SCALED_ROBOT_MIN_CAMERA_DIST
                ghost_theta = -pi/2
            elif obs.facing == Direction.SOUTH:
                ghost_x -= robot_pad
                ghost_y -= SCALED_ROBOT_WIDTH + \
                           SCALED_ROBOT_MIN_CAMERA_DIST
                ghost_theta = pi/2
            elif obs.facing == Direction.EAST:
                ghost_x += SCALED_ROBOT_MIN_CAMERA_DIST + \
                           SCALED_OBSTACLE_WIDTH + \
                           SCALED_ROBOT_WIDTH
                ghost_y -= robot_pad
                ghost_theta = -pi
            else:
                ghost_x -= SCALED_ROBOT_MIN_CAMERA_DIST + \
                           SCALED_ROBOT_WIDTH
                ghost_y += SCALED_OBSTACLE_WIDTH + \
                           robot_pad
            draw_robot(
                self.canvas,
                ghost_x, 
                ghost_y,
                ghost_theta,
                dash=(1,1),
                outline='black'
            )
        self.obstacles = obstacles


    def _display_timestep(self, dt: int):
        """Display the next location of the robot in the GUI"""
        if not self.path:
            return
        
        self.t = max(0, min(self.t + dt, len(self.path)-1))

        # erase previous state of robot
        for ref in self.prev_state:
            self.canvas.delete(ref)

        node = self.path[self.t]
        pos = node.c_pos

        if node.f != 0:
            logger.info(f'{pos},  v={node.v}, s={node.s}, g={node.g} f={node.f}')
        self.prev_state = draw_robot(self.canvas, pos.x*TK_SCALE, pos.y*TK_SCALE, pos.theta, outline='red')

        if not self.map.is_valid(pos, self.obstacles):
            logger.info(f'Collision @ {pos}')
        

    def run(self):
        """Start the GUI"""
        path = []
        prev = None

        # Discretise turns into small steps
        for node in self.path:
            s = node.s
            v = node.v

            if s == 0:
                path.append(node)
            else:
                if v == 1 and s == -1:
                    wps = WPS_FL
                elif v == 1 and s == 1:
                    wps = WPS_FR
                elif v == -1 and s == -1:
                    wps = WPS_BL
                elif v == -1 and s == 1:
                    wps = WPS_BR
                
                vv = calc_vector(prev.theta, 1)
                vh = calc_vector(prev.theta - pi/2, 1)
                vp = np.array([prev.x, prev.y])
                for dx, dy, dphi in wps[1:-1]: 
                    ppos = Position(*(vp + vv*dy + vh*dx), prev.theta + dphi)
                    path.append(Node(ppos, ppos, 0, 0))
                path.append(node)
            prev = node.c_pos

        self.path = path
        self._display_timestep(1)
        self.window.mainloop()