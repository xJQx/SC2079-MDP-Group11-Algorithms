import React from "react";
import { GRID_TOTAL_HEIGHT, GRID_TOTAL_WIDTH } from "../../../constants";
import { Position } from "../../../schemas/robot";

interface NavigationGridProps {
  robotPosition: Position;
}

export const NavigationGrid = (props: NavigationGridProps) => {
  const { robotPosition } = props;

  /**
   * Creates a HTML Grid.
   * @abstract This function will look at the state of the cell and style it accordingly. E.g.: Empty cell vs Cell with Robot.
   * @returns React.ReactNode[][] - `<td />[][]`
   * */
  const createHTMLGrid = () => {
    const grid: React.ReactNode[][] = [];

    for (let y = GRID_TOTAL_HEIGHT - 1; y >= 0; y--) {
      const currentRow: React.ReactNode[] = [];

      for (let x = 0; x < GRID_TOTAL_WIDTH; x++) {
        // Cell Contains Robot.
        if (
          robotPosition.x <= x &&
          x <= robotPosition.x + 2 &&
          robotPosition.y <= y &&
          y <= robotPosition.y + 2
        )
          currentRow.push(
            createHTMLGridCellRobot(
              x,
              y,
              x ===
                robotPosition.x +
                  convertRobotThetaToCameraOffsetBlock(
                    robotPosition.theta
                  )[0] &&
                y ===
                  robotPosition.y +
                    convertRobotThetaToCameraOffsetBlock(robotPosition.theta)[1]
                ? "camera"
                : "body"
            )
          );
        // Empty Cell
        else currentRow.push(createHTMLGridCellEmpty(x, y));
      }
      grid.push(currentRow);
    }
    return grid;
  };

  const grid = createHTMLGrid();
  addHTMLGridLables(grid);

  return (
    <div>
      {/* Grid */}
      <table>
        <tbody>
          {grid.map((row) => {
            return <tr>{row.map((column) => column)}</tr>;
          })}
        </tbody>
      </table>
    </div>
  );
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

/** Adds x-axis and y-axis labels to the Grid */
const addHTMLGridLables = (grid: React.ReactNode[][]) => {
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
const convertRobotThetaToCameraOffsetBlock = (theta: number) => {
  // -0.785 to 0.785 -> East
  if (-Math.PI / 4 < theta && theta < Math.PI / 4) {
    return [2, 1];
  }
  // 0.785 to 2.355 -> North
  else if (Math.PI / 4 <= theta && theta <= (3 * Math.PI) / 4) {
    return [1, 2];
  }
  // (2.355 to 3.14) or (-2.355 to -3.14) -> West
  else if (
    ((3 * Math.PI) / 4 < theta && theta <= Math.PI) ||
    (-Math.PI <= theta && theta < (-3 * Math.PI) / 4)
  ) {
    return [0, 1];
  }
  // -2.355 to -0.785 -> South
  else if ((-3 * Math.PI) / 4 <= theta && theta <= -Math.PI / 4) {
    return [1, 0];
  }
  return [0, 0];
};