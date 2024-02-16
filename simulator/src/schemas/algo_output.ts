import { Obstacle } from "./obstacle";
import { Position, RobotAction } from "./robot";

/** Positions that the Robot will take
 * @param x in 5cm increment
 * @param y in 5cm increment
 * @param theta in radian (positive) from 0 to 2 PI (in NSEW direction) where East = 0 radian
 */
export interface AlgoOutput {
  positions: {
    x: number; // in cm (5cm increment)
    y: number; // in cm (5cm increment)
    theta: number; // in radian (positive from 0 to 2 PI; in NSEW direction)
  }[];
  runtime: string; // in seconds
}

/** @deprecated Paths that the robot should take in the navigational area according to the algorithm used */
export interface AlgoOutputPaths {
  paths: {
    startPosition: Position;
    endPosition: Position;
    steps: RobotAction[];
  }[];
}

/**
 * @deprecated The Sequences of all the obstacles that the Robot should visit in to minimise the total distance travelled
 * @note This is only a helper algorithm output that is optional for the robot pathing.
 */
export interface AlgoOutputVisitSequences {
  visitSequences: Obstacle[];
}
