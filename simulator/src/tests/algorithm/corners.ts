import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { x: 0, y: 19, direction: ObstacleDirection.E },
  { x: 19, y: 19, direction: ObstacleDirection.S },
  { x: 19, y: 0, direction: ObstacleDirection.W },
];

export const AlgoTestCorners: AlgoTestDataInterface = {
  obstacles: obstacles,
};
