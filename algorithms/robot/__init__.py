from math import cos, sin, pi

from common.consts import ROBOT_TIME_STEP, TURNING_RADIUS


class Robot:
    """The Robot class stores the robot's current state, and facilitates calculation of new coordinates after each robot movement"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = pi/2

    def move_forward(
        self
    ) -> int:
        self.x = self.x + ROBOT_TIME_STEP*cos(self.theta) 
        self.y = self.y + ROBOT_TIME_STEP*sin(self.theta)
        # print("move forward")
        return ROBOT_TIME_STEP # returned as total distance travelled

    def move_backward(
        self
    ) -> int:
        self.x = self.x - ROBOT_TIME_STEP*cos(self.theta)
        self.y = self.y - ROBOT_TIME_STEP*sin(self.theta)
        # print("move forward")
        return ROBOT_TIME_STEP # returned as total distance travelled

    def turn_left(
        self
    ) -> int:
        arc_length = ROBOT_TIME_STEP
        self.theta = self.theta + arc_length/TURNING_RADIUS
        return arc_length
    
    def turn_right(
        self
    ) -> int:
        arc_length = ROBOT_TIME_STEP
        self.theta = self.theta - arc_length/TURNING_RADIUS
        return arc_length

    def move_forward_left(
        self
    ) -> int:
        arc_length = self.turn_left()
        distance = self.move_forward()
        path_length = arc_length + distance
        return path_length # returned as combined cost
    
    def move_forward_right(
        self
    ) -> int:
        arc_length = self.turn_right()
        distance = self.move_forward()
        path_length = arc_length + distance
        return path_length # returned as combined cost

    def move_backward_left(
        self
    ) -> int:
        arc_length = self.turn_right()
        distance = self.move_backward()
        path_length = arc_length + distance
        return path_length # returned as combined cost
    
    def move_backward_right(
        self
    ) -> int:
        arc_length = self.turn_left()
        distance = self.move_backward()
        path_length = arc_length + distance
        return path_length # returned as combined cost