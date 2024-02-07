import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { id: 1, x: 1, y: 10, d: ObstacleDirection.N },
  { id: 2, x: 9, y: 8, d: ObstacleDirection.W },
  { id: 3, x: 6, y: 0, d: ObstacleDirection.E },
  { id: 4, x: 0, y: 19, d: ObstacleDirection.E },
  { id: 5, x: 19, y: 19, d: ObstacleDirection.S },
  { id: 6, x: 19, y: 0, d: ObstacleDirection.W },
  { id: 7, x: 12, y: 17, d: ObstacleDirection.S },
];

export const AlgoTestObstacles_7: AlgoTestDataInterface = {
  obstacles: obstacles,
};
