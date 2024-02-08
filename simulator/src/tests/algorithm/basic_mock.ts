import { AlgoTestDataInterface } from ".";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";

const obstacles: Obstacle[] = [
  { id: 1, x: 15, y: 10, d: ObstacleDirection.W },
  { id: 2, x: 1, y: 18, d: ObstacleDirection.S },
];

export const AlgoTestBasicMock: AlgoTestDataInterface = {
  obstacles: obstacles,
};
