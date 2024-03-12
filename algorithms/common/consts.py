import math


INDOOR = True

# +------------------+
# | robot dimensions |
# +------------------+

ROBOT_WIDTH = 25
ROBOT_HEIGHT = 28
ROBOT_ACTUAL_WIDTH = 18.8
ROBOT_ACTUAL_HEIGHT = 23
ROBOT_VERT_OFFSET = (ROBOT_HEIGHT - ROBOT_ACTUAL_HEIGHT) / 2

# +--------------------+
# | collision checking |
# +--------------------+
# WPS: Waypoints
# Measure (Using Bottom Left of Robot)
# Indoor (SCSE Lounge)
# WPS_FL_IN = [(0, 0, 0), (1.1375, 6.125, 0), (-1.1375, 11.375, 0), (-2.8438, 15.75, 0), (-6.825, 19.25, 0), (-15.3563, 24.5, 0), (-22.75, 26.25, 1.5707963267948966)]
# WPS_FR_IN = [(0, 0, 0), (1.4217, 11.9025, 0), (6.1389, 25.3575, 0), (8.9722, 30.5325, 0), (11.8056, 34.6725, 0), (15.1111, 38.8125, 0), (19.3611, 41.9175, 0), (23.6111, 45.0225, 0), (27.8611, 48.1275, 0), (42.5, 51.75, -1.5707963267948966)]
# WPS_BR_IN = [(0, 0, 0), (0.7125, -5.8875, 0), (2.4938, -11.775, 0), (6.4125, -19.625, 0), (14.9625, -29.4375, 0), (27.7875, -36.6333, 0), (42.75, -39.25, 1.5707963267948966)]
# WPS_BL_IN = [(0, 0, 0), (-0.9613, -5.475, 0), (-3.2042, -11.315, 0), (-6.7289, -15.695, 0), (-12.1761, -18.25, 0), (-16.3415, -20.075, 0), (-22.75, -18.25, -1.5707963267948966)]

# Measure (Using Bottom Left of Robot)
# Indoor (SCSE Lab)
WPS_FL_IN = [(0, 0, 0), (1.1375, 6.125, 0), (-1.1375, 11.375, 0), (-2.8438, 15.75, 0), (-6.825, 19.25, 0), (-15.3563, 24.5, 0), (-22.75, 26.25, 1.5707963267948966)]
WPS_FR_IN = [(0, 0, 0), (1.4217, 11.9025, 0), (6.1389, 25.3575, 0), (8.9722, 30.5325, 0), (11.8056, 34.6725, 0), (15.1111, 38.8125, 0), (19.3611, 41.9175, 0), (23.6111, 45.0225, 0), (27.8611, 48.1275, 0), (43, 52, -1.5707963267948966)]
WPS_BR_IN = [(0, 0, 0), (0.7125, -5.8875, 0), (2.4938, -11.775, 0), (6.4125, -19.625, 0), (14.9625, -29.4375, 0), (27.7875, -36.6333, 0), (42.75, -39.25, 1.5707963267948966)]
WPS_BL_IN = [(0, 0, 0), (-0.9613, -5.475, 0), (-3.2042, -11.315, 0), (-6.7289, -15.695, 0), (-12.1761, -18.25, 0), (-16.3415, -20.075, 0), (-22.75, -18.25, -1.5707963267948966)]

# TODO: Measure (Using Bottom Left of Robot)
# Outdoor (SCSE Corridor)
WPS_FL_OUT = [(0, 0, 0), (1.1375, 6.125, 0), (-1.1375, 11.375, 0), (-2.8438, 15.75, 0), (-6.825, 19.25, 0), (-15.3563, 24.5, 0), (-22.75, 26.25, 1.5707963267948966)]
WPS_FR_OUT = [(0, 0, 0), (1.4217, 11.9025, 0), (6.1389, 25.3575, 0), (8.9722, 30.5325, 0), (11.8056, 34.6725, 0), (15.1111, 38.8125, 0), (19.3611, 41.9175, 0), (23.6111, 45.0225, 0), (27.8611, 48.1275, 0), (43, 52, -1.5707963267948966)]
WPS_BR_OUT = [(0, 0, 0), (0.7125, -5.8875, 0), (2.4938, -11.775, 0), (6.4125, -19.625, 0), (14.9625, -29.4375, 0), (27.7875, -36.6333, 0), (42.75, -39.25, 1.5707963267948966)]
WPS_BL_OUT = [(0, 0, 0), (-0.9613, -5.475, 0), (-3.2042, -11.315, 0), (-6.7289, -15.695, 0), (-12.1761, -18.25, 0), (-16.3415, -20.075, 0), (-22.75, -18.25, -1.5707963267948966)]

WPS_FL = WPS_FL_IN if INDOOR else WPS_FL_OUT
WPS_FR = WPS_FR_IN if INDOOR else WPS_FR_OUT
WPS_BR = WPS_BR_IN if INDOOR else WPS_BR_OUT
WPS_BL = WPS_BL_IN if INDOOR else WPS_BL_OUT

BUFFER = 5.01
OUTER_ARC_POINTS = 20
INNER_ARC_POINTS = 10

# +-------+
# | astar |
# +-------+

FL_A_IN, FL_B_IN = 15.6, 21.6 # TODO: Calculate
FR_A_IN, FR_B_IN = 35.2, 40.6 # TODO: Calculate
BR_A_IN, BR_B_IN = 42.7, 34.1 # TODO: Calculate
BL_A_IN, BL_B_IN = 21.3, 14.9 # TODO: Calculate

FL_A_OUT, FL_B_OUT = 15.1, 22.2 # TODO: Calculate
FR_A_OUT, FR_B_OUT = 33.1, 40.7 # TODO: Calculate
BR_A_OUT, BR_B_OUT = 41.6, 34 # TODO: Calculate
BL_A_OUT, BL_B_OUT = 20.8, 14.2 # TODO: Calculate

FL_A, FL_B = (FL_A_IN, FL_B_IN) if INDOOR else (FL_A_OUT, FL_B_OUT)
FR_A, FR_B = (FR_A_IN, FR_B_IN) if INDOOR else (FR_A_OUT, FR_B_OUT)
BR_A, BR_B = (BR_A_IN, BR_B_IN) if INDOOR else (BR_A_OUT, BR_B_OUT)
BL_A, BL_B = (BL_A_IN, BL_B_IN) if INDOOR else (BL_A_OUT, BL_B_OUT)

_DIST_STR = 5
DIST_BW = _DIST_STR
DIST_FW = _DIST_STR

_circum = lambda a, b: math.pi * ( 3*(a+b) - math.sqrt( (3*a + b) * (a + 3*b) ) )
# x displacement, y displacement, arc length
DIST_FL = WPS_FL[-1][0], WPS_FL[-1][1], _circum(FL_A, FL_B)/4
DIST_FR = WPS_FR[-1][0], WPS_FR[-1][1], _circum(FR_A, FR_B)/4
DIST_BL = WPS_BL[-1][0], WPS_BL[-1][1], _circum(BL_A, BL_B)/4
DIST_BR = WPS_BR[-1][0], WPS_BR[-1][1], _circum(BR_A, BR_B)/4

PENALTY_STOP = 40
MAX_THETA_ERR = math.pi / 12
MAX_X_ERR = 5, 5  # L, R (Configurable: Change to edit the node boundaries)
MAX_Y_ERR = 7.5, 35 # U, D (Configurable: Change to edit the node boundaries)

# +---------------------+
# | obstacle dimensions |
# +---------------------+

OBSTACLE_WIDTH = 10
IMG_THICKNESS = 2
EDGE_ERR = 0.1
CONE = [10, 10, 4, 40]

# +--------------------+
# | Priority obstacles |
# +--------------------+

# *_X = LEFT, RIGHT
# *_Y = UP, DOWN

FL_OUTER_IN = 41
FR_OUTER_IN = 54
BL_OUTER_IN = 47
BR_OUTER_IN = 69

FL_OUTER_OUT = 40.8
FR_OUTER_OUT = 51.6
BL_OUTER_OUT = 46.7
BR_OUTER_OUT = 63

FL_OUTER = FL_OUTER_IN if INDOOR else FL_OUTER_OUT
FR_OUTER = FR_OUTER_IN if INDOOR else FR_OUTER_OUT
BL_OUTER = BL_OUTER_IN if INDOOR else BL_OUTER_OUT
BR_OUTER = BR_OUTER_IN if INDOOR else BR_OUTER_OUT


FL_X_BOUND = [OBSTACLE_WIDTH/2 + FL_A - ROBOT_WIDTH/2 + ROBOT_HEIGHT - ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2 + ROBOT_WIDTH]

FL_Y_BOUND = [OBSTACLE_WIDTH/2 + FL_OUTER + (FL_B - FL_A) + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2]

FR_X_BOUND = [OBSTACLE_WIDTH/2, 
              OBSTACLE_WIDTH/2 + FR_A + ROBOT_WIDTH/2 + ROBOT_HEIGHT - ROBOT_VERT_OFFSET]

FR_Y_BOUND = [OBSTACLE_WIDTH/2 + FR_OUTER + (FR_B - FL_A) + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2]

BL_X_BOUND = [OBSTACLE_WIDTH/2 + BL_A - ROBOT_WIDTH/2 + ROBOT_VERT_OFFSET, 
              OBSTACLE_WIDTH/2 + BL_OUTER - (BL_A - ROBOT_WIDTH/2)] 

BL_Y_BOUND = [OBSTACLE_WIDTH/2 + ROBOT_HEIGHT, 
              OBSTACLE_WIDTH/2 + BL_B + ROBOT_WIDTH/2 - ROBOT_VERT_OFFSET]

BR_X_BOUND = [OBSTACLE_WIDTH/2 + BR_OUTER - BR_A - ROBOT_WIDTH/2, 
              OBSTACLE_WIDTH/2 + BR_A + ROBOT_WIDTH/2 + ROBOT_VERT_OFFSET]

BR_Y_BOUND = [OBSTACLE_WIDTH/2 + ROBOT_HEIGHT, 
              OBSTACLE_WIDTH/2 + BR_B + ROBOT_WIDTH/2 - ROBOT_VERT_OFFSET]

ROBOT_BTM_LEFT_CIRCLE_RAD = 2 # indicates bottom left of the robot footprint (used in algorithms/simulator)
ROBOT_MIN_CAMERA_DIST = 20

# -------- deprecated --------
ROBOT_TURNING_RADIUS = 25
# -------- ---------- --------

# +----------------+
# | map dimensions |
# +----------------+

TK_SCALE = 2
MAP_WIDTH = 200 
MAP_HEIGHT = 200
GRID_WIDTH = 5 # for display on simulator
SNAP_COORD = _DIST_STR # for cell snap (coords) 5. Max value < 1.5* min(DIST_BL, DIST_BR, ... DIST_FW)
SNAP_THETA = 15 # for cell snap (theta) 15

# +-----------------+
# | robot movements |
# +-----------------+

# -------- deprecated --------
ROBOT_TIME_STEP = 10 
TURNING_RADIUS = 25
# -------- ---------- --------

# scale values
# do not modify
SCALED_MAP_WIDTH = int(MAP_WIDTH * TK_SCALE)
SCALED_MAP_HEIGHT = int(MAP_HEIGHT * TK_SCALE)
GRID_WIDTH = int(GRID_WIDTH * TK_SCALE)
SCALED_ROBOT_WIDTH = ROBOT_WIDTH * TK_SCALE
SCALED_ROBOT_HEIGHT = ROBOT_HEIGHT * TK_SCALE
SCALED_ROBOT_TURNING_RADIUS = ROBOT_TURNING_RADIUS * TK_SCALE
ROBOT_BTM_LEFT_CIRCLE_RAD *= TK_SCALE
SCALED_ROBOT_MIN_CAMERA_DIST = ROBOT_MIN_CAMERA_DIST * TK_SCALE
SCALED_OBSTACLE_WIDTH = OBSTACLE_WIDTH * TK_SCALE
IMG_THICKNESS *= TK_SCALE