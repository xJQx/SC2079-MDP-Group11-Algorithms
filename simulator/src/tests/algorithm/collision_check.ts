import { AlgoTestDataInterface } from ".";
import { ObstacleDirection } from "../../schemas/obstacle";

export const AlgoTestCollisionCheck_A: AlgoTestDataInterface = {
  obstacles: [
    { id: 1, x: 1, y: 13, d: ObstacleDirection.S },
    { id: 2, x: 7, y: 13, d: ObstacleDirection.W },
  ],
};

export const AlgoTestCollisionCheck_B: AlgoTestDataInterface = {
  obstacles: [
    { id: 1, x: 10, y: 15, d: ObstacleDirection.S },
    { id: 2, x: 10, y: 7, d: ObstacleDirection.N },
  ],
};

export const AlgoTestCollisionCheck_C: AlgoTestDataInterface = {
  obstacles: [
    { id: 1, x: 9, y: 5, d: ObstacleDirection.W },
    { id: 2, x: 9, y: 9, d: ObstacleDirection.E },
    { id: 2, x: 17, y: 7, d: ObstacleDirection.W },
  ],
};
