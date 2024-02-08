/* eslint-disable @typescript-eslint/no-unused-vars */

import { Position, RobotDirection } from "../schemas/robot";

// Robot's Environment - Grid Format
const WIDTH_CM = 200;
const HEIGHT_CM = 200;
export const GRID_BLOCK_SIZE_CM = 10; // *Size of each block in cm

const ALGO_GRID_BLOCK_SIZE_CM = 5; // Size of each block in cm (used in the algo backend)
export const ALGO_GRID_BLOCK_SIZE_MULTIPLIER =
  GRID_BLOCK_SIZE_CM / ALGO_GRID_BLOCK_SIZE_CM; // 2

export const GRID_TOTAL_WIDTH = WIDTH_CM / GRID_BLOCK_SIZE_CM; // 40
export const GRID_TOTAL_HEIGHT = HEIGHT_CM / GRID_BLOCK_SIZE_CM; // 40

export const START_ZONE_X = 0;
export const START_ZONE_Y = 0;

// Obstacles
const OBSTACLE_WIDTH_CM = 10;
const OBSTACLE_HEIGHT_CM = 10;

export const OBSTACLE_GRID_WIDTH = OBSTACLE_WIDTH_CM / GRID_BLOCK_SIZE_CM; // 1
export const OBSTACLE_GRID_HEIGHT = OBSTACLE_HEIGHT_CM / GRID_BLOCK_SIZE_CM; // 1

// Robot's Footprint (Can be reduced according to measurements)
const ROBOT_WIDTH_CM = 30;
const ROBOT_HEIGHT_CM = 30;

export const ROBOT_GRID_WIDTH = ROBOT_WIDTH_CM / GRID_BLOCK_SIZE_CM; // 3
export const ROBOT_GRID_HEIGHT = ROBOT_HEIGHT_CM / GRID_BLOCK_SIZE_CM; // 3

export const ROBOT_INITIAL_DIRECTION = Math.PI / 2;
export const ROBOT_INITIAL_POSITION: Position = {
  x: 0,
  y: 0,
  theta: ROBOT_INITIAL_DIRECTION,
};

/** @deprecated  Robot Turning Movement */
export const ROBOT_TURNING_RADIUS_CM = 30;
export const ROBOT_GRID_TURNING_RADIUS =
  ROBOT_TURNING_RADIUS_CM / GRID_BLOCK_SIZE_CM; // 6

/** @deprecated */
interface turnOffsetInterface {
  [RobotDirection.N]: {
    [RobotDirection.N]: [number, number];
    [RobotDirection.S]: [number, number];
    [RobotDirection.E]: [number, number];
    [RobotDirection.W]: [number, number];
  };
  [RobotDirection.S]: {
    [RobotDirection.N]: [number, number];
    [RobotDirection.S]: [number, number];
    [RobotDirection.E]: [number, number];
    [RobotDirection.W]: [number, number];
  };
  [RobotDirection.E]: {
    [RobotDirection.N]: [number, number];
    [RobotDirection.S]: [number, number];
    [RobotDirection.E]: [number, number];
    [RobotDirection.W]: [number, number];
  };
  [RobotDirection.W]: {
    [RobotDirection.N]: [number, number];
    [RobotDirection.S]: [number, number];
    [RobotDirection.E]: [number, number];
    [RobotDirection.W]: [number, number];
  };
}

/**
 * @deprecated Maps offsets between two robot direction configuration
 * @key [RobotDirection.FROM]: { [RobotDirection.TO]: [x, y] }
 * @returns [x, y] offsets
 * */
export const clockwiseOffsets: turnOffsetInterface = {
  [RobotDirection.N]: {
    [RobotDirection.E]: [ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.S]: [0, -ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.W]: [
      -ROBOT_GRID_TURNING_RADIUS,
      -ROBOT_GRID_TURNING_RADIUS,
    ],
    [RobotDirection.N]: [0, 0],
  },
  [RobotDirection.E]: {
    [RobotDirection.S]: [ROBOT_GRID_TURNING_RADIUS, -ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.W]: [0, -ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.N]: [
      -ROBOT_GRID_TURNING_RADIUS,
      -ROBOT_GRID_TURNING_RADIUS,
    ],
    [RobotDirection.E]: [0, 0],
  },
  [RobotDirection.S]: {
    [RobotDirection.W]: [
      -ROBOT_GRID_TURNING_RADIUS,
      -ROBOT_GRID_TURNING_RADIUS,
    ],
    [RobotDirection.N]: [-ROBOT_GRID_TURNING_RADIUS * 2, 0],
    [RobotDirection.E]: [-ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.S]: [0, 0],
  },
  [RobotDirection.W]: {
    [RobotDirection.N]: [-ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.E]: [0, ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.S]: [ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.W]: [0, 0],
  },
};
export const antiClockwiseOffsets = {
  [RobotDirection.N]: {
    [RobotDirection.W]: [
      -ROBOT_GRID_TURNING_RADIUS,
      -ROBOT_GRID_TURNING_RADIUS,
    ],
    [RobotDirection.S]: [0, -ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.E]: [ROBOT_GRID_TURNING_RADIUS, -ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.N]: [0, 0],
  },
  [RobotDirection.W]: {
    [RobotDirection.S]: [
      -ROBOT_GRID_TURNING_RADIUS,
      -ROBOT_GRID_TURNING_RADIUS,
    ],
    [RobotDirection.E]: [0, -ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.N]: [ROBOT_GRID_TURNING_RADIUS, -ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.W]: [0, 0],
  },
  [RobotDirection.S]: {
    [RobotDirection.E]: [ROBOT_GRID_TURNING_RADIUS, -ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.N]: [ROBOT_GRID_TURNING_RADIUS * 2, 0],
    [RobotDirection.W]: [ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.S]: [0, 0],
  },
  [RobotDirection.E]: {
    [RobotDirection.N]: [ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.W]: [0, ROBOT_GRID_TURNING_RADIUS * 2],
    [RobotDirection.S]: [-ROBOT_GRID_TURNING_RADIUS, ROBOT_GRID_TURNING_RADIUS],
    [RobotDirection.E]: [0, 0],
  },
};

// Grid Animation
export const GRID_ANIMATION_SPEED = 100; // in milli-seconds
export const ARTIFICAL_DELAY_CURVE = 2; // per gird timestep
export const ARTIFICAL_DELAY_SCAN = 2; // per gird timestep
