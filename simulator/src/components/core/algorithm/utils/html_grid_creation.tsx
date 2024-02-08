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
  obstacles: Obstacle[]
) => {
  const grid: React.ReactNode[][] = [];

  for (let y = GRID_TOTAL_HEIGHT - 1; y >= 0; y--) {
    const currentRow: React.ReactNode[] = [];

    for (let x = 0; x < GRID_TOTAL_WIDTH; x++) {
      // Cell Contains Robot.
      if (
        robotPosition.x <= x &&
        x <= robotPosition.x + (ROBOT_GRID_WIDTH - 1) &&
        robotPosition.y <= y &&
        y <= robotPosition.y + (ROBOT_GRID_HEIGHT - 1)
      )
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
            )[0].d
          )
        );
      }
      // Empty Cell
      else currentRow.push(createHTMLGridCellEmpty(x, y));
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
const createHTMLGridCellEmpty = (x: number, y: number) => {
  return (
    <td id={`cell-${x}-${y}`} className="border border-orange-900 w-8 h-8" />
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
  direction: ObstacleDirection
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

  return (
    <td
      id={`cell-${x}-${y}`}
      className={`border border-orange-900 w-8 h-8 align-middle text-center bg-amber-400 ${imageFaceBorderClassName}`}
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
 * Converts a Robot's Theta rotation to the associated Camera Offset on the grid
 * @returns (x, y) offset of the robot's camera from the bottom left corner of the robot
 */
export const convertRobotThetaToCameraOffsetBlock = (theta: number) => {
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
