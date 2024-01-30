import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { x: 1, y: 10, direction: ObstacleDirection.N },
  { x: 9, y: 8, direction: ObstacleDirection.W },
  { x: 6, y: 0, direction: ObstacleDirection.E },
  { x: 0, y: 19, direction: ObstacleDirection.E },
  { x: 19, y: 19, direction: ObstacleDirection.S },
  { x: 19, y: 0, direction: ObstacleDirection.W },
  { x: 12, y: 17, direction: ObstacleDirection.S },
];

export const AlgoTestObstacles_7: AlgoTestDataInterface = {
  obstacles: obstacles,
};
