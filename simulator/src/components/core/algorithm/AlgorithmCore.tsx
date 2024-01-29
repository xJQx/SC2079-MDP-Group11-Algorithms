import React from "react";
import { NavigationGrid } from "./NavigationGrid";
import { CoreContainter } from "../CoreContainter";
import { Position } from "../../../schemas/robot";
import { ROBOT_INITIAL_DIRECTION } from "../../../constants";

export const AlgorithmCore = () => {
  const robotPosition: Position = {
    x: 0,
    y: 0,
    theta: ROBOT_INITIAL_DIRECTION,
  };

  return (
    <CoreContainter title="Algorithm Simulator">
      <NavigationGrid robotPosition={robotPosition} />
    </CoreContainter>
  );
};
