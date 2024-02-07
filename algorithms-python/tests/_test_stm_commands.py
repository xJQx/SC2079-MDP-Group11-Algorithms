from arena.map import Map, Obstacle
from common.enums import Movement, Direction
from common.types import Position
from robot.stm_commands import backtracking_smooth_path
from path_finding.hybrid_astar import Node

def send_commands():
    obstacles = [
        Obstacle(50, 150, Direction.EAST),
        Obstacle(30, 80, Direction.SOUTH),
        Obstacle(120, 30, Direction.EAST),
        Obstacle(90, 110, Direction.WEST),
        Obstacle(150, 90, Direction.NORTH)
    ]
    mp = Map(obstacles)
    
    
    