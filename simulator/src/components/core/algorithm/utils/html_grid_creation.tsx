import {
  GRID_TOTAL_HEIGHT,
  GRID_TOTAL_WIDTH,
  ROBOT_GRID_HEIGHT,
  ROBOT_GRID_WIDTH,
} from "../../../../constants";
import { Obstacle, ObstacleDirection } from "../../../../schemas/obstacle";
import { Position, RobotDirection } from "../../../../schemas/robot";
import { convertThetaToDirection } from "./conversions";

/**
 * Creates a HTML Grid.
 * @abstract This function will look at the state of the cell and style it accordingly. E.g.: Empty cell vs Cell with Robot.
 * @returns React.ReactNode[][] - `<td />[][]`
 * */
export const createHTMLGrid = (
  robotPosition: Position,
  obstacles: Obstacle[],
  canAddObstacle: boolean,
  handleAddObstacle: (x: number, y: number, d: number) => void,
  handleChangeObstacleDirection: (x: number, y: number, new_d: number) => void
) => {
  const grid: React.ReactNode[][] = [];

  for (let y = GRID_TOTAL_HEIGHT - 1; y >= 0; y--) {
    const currentRow: React.ReactNode[] = [];

    for (let x = 0; x < GRID_TOTAL_WIDTH; x++) {
      // Cell Contains Robot.
      if (isRobotCell(robotPosition, x, y))
        currentRow.push(
          createHTMLGridCellRobot(
            x,
            y,
            x ===
              robotPosition.x +
                convertRobotThetaToCameraOffsetBlock(robotPosition.theta)[0] &&
              y ===
                robotPosition.y +
                  convertRobotThetaToCameraOffsetBlock(robotPosition.theta)[1]
              ? "camera"
              : "body"
          )
        );
      // Cell Contains an Obstacle
      else if (
        obstacles.filter((obstacle) => obstacle.x === x && obstacle.y === y)
          .length > 0
      ) {
        currentRow.push(
          createHTMLGridCellObstacle(
            x,
            y,
            obstacles.filter(
              (obstacle) => obstacle.x === x && obstacle.y === y
            )[0].d,
            canAddObstacle,
            handleChangeObstacleDirection
          )
        );
      }
      // Empty Cell
      else
        currentRow.push(
          createHTMLGridCellEmpty(x, y, canAddObstacle, handleAddObstacle)
        );
    }
    grid.push(currentRow);
  }
  return grid;
};

// ---------- Helper Functions - HTML ---------- //
/**
 * Creates a `<td />` for an empty cell
 * @used_by createHTMLGrid()
 */
const createHTMLGridCellEmpty = (
  x: number,
  y: number,
  canAddObstacle: boolean,
  handleAddObstacle: (x: number, y: number, d: number) => void
) => {
  if (!canAddObstacle) {
    return (
      <td id={`cell-${x}-${y}`} className="border border-orange-900 w-8 h-8" />
    );
  }

  return (
    <td
      id={`cell-${x}-${y}`}
      className="border border-orange-900 w-8 h-8 cursor-pointer hover:bg-amber-400 hover:border-t-4 hover:border-t-red-700"
      onClick={() => handleAddObstacle(x, y, 1)} // Default North Facing
      title="Add obstacle"
    />
  );
};

/**
 * Creates a `<td />` for a cell that contains the Robot's body
 * @used_by createHTMLGrid()
 */
const createHTMLGridCellRobot = (
  x: number,
  y: number,
  type: "camera" | "body"
) => {
  return (
    <td
      id={`cell-${x}-${y}`}
      className={`border-2 border-orange-900 w-8 h-8 align-middle text-center ${
        type === "body" ? "bg-green-300" : "bg-blue-400"
      }`}
    />
  );
};

/**
 * Creates a `<td />` for a cell that contains an Obstacle
 * @used_by createHTMLGrid()
 */
const createHTMLGridCellObstacle = (
  x: number,
  y: number,
  direction: ObstacleDirection,
  canChangeObstacleDirection: boolean,
  handleChangeObstacleDirection: (x: number, y: number, new_d: number) => void
) => {
  let imageFaceBorderClassName = "";
  switch (direction) {
    case ObstacleDirection.N:
      imageFaceBorderClassName = "border-t-4 border-t-red-700";
      break;
    case ObstacleDirection.S:
      imageFaceBorderClassName = "border-b-4 border-b-red-700";
      break;
    case ObstacleDirection.E:
      imageFaceBorderClassName = "border-r-4 border-r-red-700";
      break;
    case ObstacleDirection.W:
      imageFaceBorderClassName = "border-l-4 border-l-red-700";
      break;
  }

  if (!canChangeObstacleDirection) {
    return (
      <td
        id={`cell-${x}-${y}`}
        className={`border border-orange-900 w-8 h-8 align-middle text-center bg-amber-400 ${imageFaceBorderClassName}`}
      />
    );
  }

  return (
    <td
      id={`cell-${x}-${y}`}
      className={`border border-orange-900 w-8 h-8 align-middle text-center bg-amber-400 ${imageFaceBorderClassName} cursor-pointer hover:bg-amber-500`}
      title="Change obstacle direction"
      onClick={() =>
        handleChangeObstacleDirection(x, y, (direction.valueOf() % 4) + 1)
      }
    />
  );
};

/** Adds x-axis and y-axis labels to the Grid */
export const addHTMLGridLables = (grid: React.ReactNode[][]) => {
  grid.forEach((row, index) =>
    row.unshift(
      <td className="font-bold pr-2">{GRID_TOTAL_HEIGHT - index - 1}</td>
    )
  );

  const gridColumnLabels: React.ReactNode[] = [];
  for (let c = -1; c < GRID_TOTAL_WIDTH; c++) {
    if (c === -1) gridColumnLabels.push(<td />);
    else
      gridColumnLabels.push(
        <td className="font-bold pt-2 text-center">{c}</td>
      );
  }
  grid.push(gridColumnLabels);
  return grid;
};

// ---------- Helper Functions - Calculations ---------- //
/**
 * @deprecated Fixed Bottom Left (x, y) area occupied by Robot as Robot's current position regardless of Robot's facing.
 * Converts a Robot's Theta rotation to the associated Camera Offset on the grid
 * @returns (x, y) offset of the robot's camera from the bottom left corner of the robot
 */
export const _convertRobotThetaToCameraOffsetBlock = (theta: number) => {
  const robotDirection = convertThetaToDirection(theta);
  // East
  if (robotDirection === RobotDirection.E) {
    return [2, 1];
  }
  // North
  else if (robotDirection === RobotDirection.N) {
    return [1, 2];
  }
  // West
  else if (robotDirection === RobotDirection.W) {
    return [0, 1];
  }
  // South
  else if (robotDirection === RobotDirection.S) {
    return [1, 0];
  }
  return [0, 0];
};

/**
 * Used Bottom Left of Robot's Body as Robot's current (x, y) position.
 * Converts a Robot's Theta rotation to the associated Camera Offset on the grid
 * @returns (x, y) offset of the robot's camera from the bottom left corner of the robot
 */
export const convertRobotThetaToCameraOffsetBlock = (theta: number) => {
  const robotDirection = convertThetaToDirection(theta);
  // East
  if (robotDirection === RobotDirection.E) {
    return [2, -1];
  }
  // North
  else if (robotDirection === RobotDirection.N) {
    return [1, 2];
  }
  // West
  else if (robotDirection === RobotDirection.W) {
    return [-2, 1];
  }
  // South
  else if (robotDirection === RobotDirection.S) {
    return [-1, -2];
  }
  return [0, 0];
};

/**
 * Checks if current cell is occupied by a Robot based on it's (x, y) position and facing.
 * @location
 */
export const isRobotCell = (
  robotPosition: Position,
  cell_x: number,
  cell_y: number
) => {
  const robotDirection: RobotDirection = convertThetaToDirection(
    robotPosition.theta
  );

  switch (robotDirection) {
    case RobotDirection.N:
      if (
        robotPosition.x <= cell_x &&
        cell_x <= robotPosition.x + (ROBOT_GRID_WIDTH - 1) &&
        robotPosition.y <= cell_y &&
        cell_y <= robotPosition.y + (ROBOT_GRID_HEIGHT - 1)
      ) {
        return true;
      } else {
        return false;
      }
    case RobotDirection.S:
      if (
        robotPosition.x - (ROBOT_GRID_WIDTH - 1) <= cell_x &&
        cell_x <= robotPosition.x &&
        robotPosition.y - (ROBOT_GRID_HEIGHT - 1) <= cell_y &&
        cell_y <= robotPosition.y
      ) {
        return true;
      } else {
        return false;
      }
    case RobotDirection.E:
      if (
        robotPosition.x <= cell_x &&
        cell_x <= robotPosition.x + (ROBOT_GRID_WIDTH - 1) &&
        robotPosition.y - (ROBOT_GRID_HEIGHT - 1) <= cell_y &&
        cell_y <= robotPosition.y
      ) {
        return true;
      } else {
        return false;
      }
    case RobotDirection.W:
      if (
        robotPosition.x - (ROBOT_GRID_WIDTH - 1) <= cell_x &&
        cell_x <= robotPosition.x &&
        robotPosition.y <= cell_y &&
        cell_y <= robotPosition.y + (ROBOT_GRID_HEIGHT - 1)
      ) {
        return true;
      } else {
        return false;
      }
    default:
      return false;
  }
};
