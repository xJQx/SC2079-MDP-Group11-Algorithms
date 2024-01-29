import {
  GRID_BLOCK_SIZE_CM,
  ROBOT_INITIAL_DIRECTION,
} from "../../../../constants";
import { AlgoOutputPaths } from "../../../../schemas/algo_output";
import {
  Position,
  RobotActionEnum,
  RobotDirection,
} from "../../../../schemas/robot";
import { convertThetaToDirection } from "./conversions";

/** Converts algorithm's output paths into step-wise Robot's `Positions` */
export const convertPathToStepwisePosition = (
  paths: AlgoOutputPaths["paths"]
) => {
  let tempRobotPosition: Position = {
    x: 0,
    y: 0,
    theta: ROBOT_INITIAL_DIRECTION,
  };
  let robotPositions: Position[] = [
    { x: 0, y: 0, theta: ROBOT_INITIAL_DIRECTION },
  ];

  paths.forEach((path) =>
    path.steps.forEach((step) => {
      switch (step.type) {
        case RobotActionEnum.MoveStraight:
          robotPositions = robotPositions.concat(
            handleMoveStraightAction(
              tempRobotPosition,
              step.distance_straight ?? 0
            )
          );
          tempRobotPosition = robotPositions[robotPositions.length - 1];
          break;
        case RobotActionEnum.MoveBack:
          robotPositions = robotPositions.concat(
            handleMoveStraightAction(
              tempRobotPosition,
              step.distance_straight ?? 0,
              false
            )
          );
          tempRobotPosition = robotPositions[robotPositions.length - 1];
          break;
        case RobotActionEnum.Scan:
          robotPositions = robotPositions.concat(handleScanAction());
          break;
      }
    })
  );
  return robotPositions;
};

/**
 * Converts MoveStraight from total straight_distance (cm) to `Position[]` for each timestep / cell movement
 * @param forward Set to `false` if robot is taking MoveBack action
 * @returns Position[]
 * */
export const handleMoveStraightAction = (
  startPosition: Position,
  distance_straight: number,
  forward: boolean = true
) => {
  const robotPositions: Position[] = [];

  let currentPosition: Position = {
    x: startPosition.x,
    y: startPosition.y,
    theta: startPosition.theta,
  };
  let distanceLeft = distance_straight;
  const robotDirection = convertThetaToDirection(startPosition.theta);

  while (distanceLeft > 0) {
    let currentPositionTemp: Position = {
      x: currentPosition.x,
      y: currentPosition.y,
      theta: currentPosition.theta,
    };
    switch (robotDirection) {
      case RobotDirection.N:
        currentPositionTemp.y += forward ? 1 : -1;
        break;
      case RobotDirection.S:
        currentPositionTemp.y += forward ? -1 : 1;
        break;
      case RobotDirection.E:
        currentPositionTemp.x += forward ? 1 : -1;
        break;
      case RobotDirection.W:
        currentPositionTemp.x += forward ? -1 : 1;
        break;
    }
    robotPositions.push(currentPositionTemp);
    currentPosition = currentPositionTemp;
    distanceLeft -= GRID_BLOCK_SIZE_CM;
  }

  return robotPositions;
};

/**
 * Converts MoveStraight from total straight_distance (cm) to `Position[]` for each timestep / cell movement
 * @returns Position[]
 * */
export const handleMoveBackAction = (
  startPosition: Position,
  distance_straight: number
) => {
  const robotPositions: Position[] = [];

  let currentPosition: Position = {
    x: startPosition.x,
    y: startPosition.y,
    theta: startPosition.theta,
  };
  let distanceLeft = distance_straight;
  const robotDirection = convertThetaToDirection(startPosition.theta);

  while (distanceLeft > 0) {
    let currentPositionTemp: Position = {
      x: currentPosition.x,
      y: currentPosition.y,
      theta: currentPosition.theta,
    };
    switch (robotDirection) {
      case RobotDirection.N:
        currentPositionTemp.y += 1;
        break;
      case RobotDirection.S:
        currentPositionTemp.y -= 1;
        break;
      case RobotDirection.E:
        currentPositionTemp.x += 1;
        break;
      case RobotDirection.W:
        currentPositionTemp.x -= 1;
        break;
    }
    robotPositions.push(currentPositionTemp);
    currentPosition = currentPositionTemp;
    distanceLeft -= GRID_BLOCK_SIZE_CM;
  }

  return robotPositions;
};

/**
 * Converts Scan to `Position`, where x = -1, y = -1, theta = -1.
 * @returns Position[] with 2 `Position` to simulate scanning action delay
 * @note (-1, -1, -1) means scanning done
 * */
export const handleScanAction = () => {
  const robotPositionScanConfigurations: Position[] = [
    { x: -1, y: -1, theta: -2 },
    { x: -1, y: -1, theta: -1 },
  ];

  return robotPositionScanConfigurations;
};
