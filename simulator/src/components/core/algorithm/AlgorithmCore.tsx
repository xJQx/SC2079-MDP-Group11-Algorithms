import React from "react";
import { NavigationGrid } from "./NavigationGrid";
import { CoreContainter } from "../CoreContainter";
import { Position } from "../../../schemas/robot";
import { ROBOT_INITIAL_DIRECTION } from "../../../constants";
import { Obstacle, ObstacleDirection } from "../../../schemas/obstacle";

export const AlgorithmCore = () => {
  const robotPosition: Position = {
    x: 0,
    y: 0,
    theta: ROBOT_INITIAL_DIRECTION,
  };
  const obstacles: Obstacle[] = [
    { x: 10, y: 10, direction: ObstacleDirection.W },
    { x: 1, y: 18, direction: ObstacleDirection.S },
  ];

  return (
    <CoreContainter title="Algorithm Simulator">
      <NavigationGrid robotPosition={robotPosition} obstacles={obstacles} />
    </CoreContainter>
  );
};
