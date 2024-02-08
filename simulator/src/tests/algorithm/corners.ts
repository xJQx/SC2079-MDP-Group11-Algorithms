import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { id: 1, x: 1, y: 18, d: ObstacleDirection.E },
  { id: 2, x: 18, y: 18, d: ObstacleDirection.S },
  { id: 3, x: 18, y: 1, d: ObstacleDirection.W },
];

export const AlgoTestCorners: AlgoTestDataInterface = {
  obstacles: obstacles,
};
