import React from "react";
import { Position } from "../../../schemas/robot";
import { Obstacle } from "../../../schemas/obstacle";
import { addHTMLGridLables, createHTMLGrid } from "./utils/html_grid_creation";

interface NavigationGridProps {
  robotPosition: Position;
  obstacles: Obstacle[];
}

export const NavigationGrid = (props: NavigationGridProps) => {
  const { robotPosition, obstacles } = props;

  const grid = createHTMLGrid(robotPosition, obstacles);
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
