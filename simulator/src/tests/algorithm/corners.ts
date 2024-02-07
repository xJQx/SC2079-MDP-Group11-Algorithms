import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { id: 1, x: 0, y: 19, d: ObstacleDirection.E },
  { id: 2, x: 19, y: 19, d: ObstacleDirection.S },
  { id: 3, x: 19, y: 0, d: ObstacleDirection.W },
];

export const AlgoTestCorners: AlgoTestDataInterface = {
  obstacles: obstacles,
};
