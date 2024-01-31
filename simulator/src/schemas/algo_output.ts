import { Obstacle } from "./obstacle";
import { Position, RobotAction } from "./robot";

/** Paths that the robot should take in the navigational area according to the algorithm used */
export interface AlgoOutputPaths {
  paths: {
    startPosition: Position;
    endPosition: Position;
    steps: RobotAction[];
  }[];
}

/**
 * The Sequences of all the obstacles that the Robot should visit in to minimise the total distance travelled
 * @note This is only a helper algorithm output that is optional for the robot pathing.
 */
export interface AlgoOutputVisitSequences {
  visitSequences: Obstacle[];
}
