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


def test_straight_fwd(collision_mp):
    st1 = Position(60, 80-ROBOT_HEIGHT-DIST_FW-1, pi/2)
    st2 = Position(60, 80-ROBOT_HEIGHT-DIST_FW+1, pi/2)
    c1 = has_collision(st1, Movement.FWD, collision_mp)
    c2 = has_collision(st2, Movement.FWD, collision_mp)
    # sim = Simulator(collision_mp)
    # sim.path.append(Node(st2, st2, 0, 0))
    assert c1 == False
    assert c2 == True
    # sim.run()


def test_straight_bwd(collision_mp):
    st1 = Position(60, 80+OBSTACLE_WIDTH+DIST_BW+1, pi/2)
    st2 = Position(60, 80+OBSTACLE_WIDTH+DIST_BW-1, pi/2)
    c1 = has_collision(st1, Movement.BWD, collision_mp)
    c2 = has_collision(st2, Movement.BWD, collision_mp)
    assert c1 == False
    assert c2 == True


def test_forward_right_collide(collision_sim, collision_mp):
    ps = (
        Position(60, 45, pi/2),
        Position(30, 50, pi/2),
        Position(40, 80, pi/2),
        Position(16, 55, pi/2),
        Position(70, 45, pi/2)
    )
    
    for p in ps:
        collision_sim.path.append(Node(p, p, 0, 0))
        
        v_st = np.array([p.x, p.y])
        v_u = calc_vector(p.theta - pi/2, 1)
        v_r = calc_vector(p.theta, 1)
        
        for wp in WPS_FR:
            new_p = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), p.theta + wp[2])
            collision_sim.path.append(Node(p, new_p, 0, 0))
        assert has_collision(p, Movement.FWD_RIGHT, collision_mp) == True
    # collision_sim.run()


def test_forward_right_miss(collision_sim, collision_mp):
    ps = (
        Position(20, 92, 0),
        Position(40, 15, pi/2),
        # TODO: Check if this is considered a collision
        Position(80, 80, pi/2), # This obstacle is being considered a collision
        Position(30, 96, pi/2)
    )
    
    for p in ps:
        collision_sim.path.append(Node(p, p, 0, 0))
        v_st = np.array([p.x, p.y])
        v_u = calc_vector(p.theta - pi/2, 1)
        v_r = calc_vector(p.theta, 1)

        for wp in WPS_FR:
            new_p = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), (p.theta + wp[2]) % (2*pi))
            collision_sim.path.append(Node(p, new_p, 0, 0))
        # assert has_collision(p, Movement.FWD_RIGHT, collision_mp) == False
    collision_sim.run()


def test_forward_left_collide(collision_sim_2, collision_mp_2):
    ps = (
        Position(110, 140, pi),
        Position(110, 140, pi),
        Position(115, 140, pi),
    )
    
    for p in ps:
        print("POSITION: ")
        print(p)
        collision_sim_2.path.append(Node(p, p, 0, 0))
        
        v_st = np.array([p.x, p.y])
        v_u = calc_vector(p.theta - pi/2, 1)
        v_r = calc_vector(p.theta, 1)
        
        for wp in WPS_FL:
            new_p = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), (p.theta + wp[2]) % (2*pi))
            collision_sim_2.path.append(Node(p, new_p, 0, 0))
        assert has_collision(p, Movement.FWD_LEFT, collision_mp_2) == True
    # collision_sim_2.run()


def test_backward_right_collide(collision_sim, collision_mp):
    ps = (
        Position(80, 95, pi/2),
    )
    
    for p in ps:
        collision_sim.path.append(Node(p, p, 0, 0))
        
        v_st = np.array([p.x, p.y])
        v_u = calc_vector(p.theta - pi/2, 1)
        v_r = calc_vector(p.theta, 1)
        
        for wp in WPS_BR:
            new_p = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), (p.theta + wp[2]) % (2*pi))
            collision_sim.path.append(Node(p, new_p, 0, 0))
        assert has_collision(p, Movement.BWD_RIGHT, collision_mp) == True
    # collision_sim.run()


def test_backward_left_collide(collision_sim_2, collision_mp_2):
    ps = (
        Position(33.2, 92.8, pi/2),
    )
    
    for p in ps:
        collision_sim_2.path.append(Node(p, p, 0, 0))
        
        v_st = np.array([p.x, p.y])
        v_u = calc_vector(p.theta - pi/2, 1)
        v_r = calc_vector(p.theta, 1)
        
        for wp in WPS_BL:
            new_p = Position(*(v_st + wp[0]*v_u + wp[1]*v_r), (p.theta + wp[2]) % (2*pi))
            collision_sim_2.path.append(Node(p, new_p, 0, 0))
        assert has_collision(p, Movement.BWD_LEFT, collision_mp_2) == False
    # collision_sim_2.run()

# def test_straight_fwd_upwards():
#     obstacles = [Obstacle(60, 80, Direction.NORTH)]
#     mp = Map(obstacles)
#     st = Position(50, 40, pi/2)
#     sim = Simulator(mp)
#     collision = has_collision(st, Movement.FWD, mp, 10)
#     # sim.run()
#     assert collision == False

# def test_straight_fwd_sideways():
#     obstacles = [Obstacle(120, 40, Direction.WEST)]
#     mp = Map(obstacles)
#     st = Position(60, 40, 0)
#     sim = Simulator(mp)
#     collision = has_collision(st, Movement.FWD, mp, 33)
#     # sim.run()
#     assert collision == True

# def test_straight_bwd_reverse():
#     obstacles = [Obstacle(30, 50, Direction.NORTH)]
#     mp = Map(obstacles)
#     st = Position(50, 40, -pi/2)
#     sim = Simulator(mp)
#     sim.path.append(Node(st, st, 0, 0))
#     collision = has_collision(st, Movement.BWD, mp, 15)
#     assert collision == True
#     # sim.run()

# def test_straight_bwd():
#     obstacles = [Obstacle(60, 20, Direction.NORTH)]
#     mp = Map(obstacles)
#     st = Position(50, obstacles[0].y+DIST_BW, pi/2)
#     # sim = Simulator(mp)
#     # sim.path.append(Node(st, st, 0, 0))
#     collision = has_collision(st, Movement.BWD, mp)
#     assert collision == True
# #     sim.run()

# def test_straight_bwd_sideways():
#     obstacles = [Obstacle(140, 20, Direction.SOUTH)]
#     mp = Map(obstacles)
#     st = Position(120, 20, pi)
#     # sim = Simulator(mp)
#     # sim.path.append(Node(st, st, 0, 0))
#     collision = has_collision(st, Movement.BWD, mp, 21)
#     # sim.run()
#     assert collision == True

# def test_straight_fwd_left_with_obstacle():
#     # Test when there is an obstacle in the path
#     obstacles = [Obstacle(40, 80, Direction.NORTH), Obstacle(180, 180, Direction.SOUTH)]  # An obstacle at (40, 50) facing NORTH
#     mp = Map(obstacles)
#     st = Position(50, 40, pi/2)  # Facing upward
#     sim = Simulator(mp)
#     sim.path.append(Node(st, st, 0, 0))
#     collision = has_collision(st, Movement.FWD_LEFT, mp)
#     # sim.run()
#     assert collision == True  # Collision should occur

# def test_straight_bwd_left_with_obstacle():
#     # Test when there is an obstacle in the path
#     obstacles = [Obstacle(40, 30, Direction.NORTH)]  # An obstacle at (40, 50) facing NORTH
#     mp = Map(obstacles)
#     st = Position(50, 40, pi/2)  # Facing upward
#     sim = Simulator(mp)
#     collision = has_collision(st, Movement.BWD_LEFT, mp)
#     # sim.run()
#     assert collision == True  # Collision should occur

# def test_straight_fwd_right_with_obstacle():
#     # Test when there is an obstacle in the path
#     obstacles = [Obstacle(60, 80, Direction.NORTH)]  # An obstacle at (60, 80) facing NORTH
#     mp = Map(obstacles)
#     st = Position(50, 40, pi/2)  # Facing upward
#     sim = Simulator(mp)
#     collision = has_collision(st, Movement.FWD_RIGHT, mp)
#     # sim.run()
#     assert collision == True  # Collision should occur

# def test_straight_bwd_right_with_obstacle():
#     # Test when there is an obstacle in the path
#     obstacles = [Obstacle(60, 80, Direction.NORTH)]  # An obstacle at (60, 80) facing NORTH
#     mp = Map(obstacles)
#     st = Position(50, 40, pi/2)  # Facing upward
#     sim = Simulator(mp)
#     collision = has_collision(st, Movement.BWD_RIGHT, mp)
#     # sim.run()
#     assert collision == False
