import { AlgoTestDataInterface } from ".";
import { ObstacleDirection } from "../../schemas/obstacle";

export const AlgoTestShapes_V: AlgoTestDataInterface = {
  obstacles: [
    { id: 1, x: 2, y: 18, d: ObstacleDirection.S },
    { id: 2, x: 10, y: 2, d: ObstacleDirection.N },
    { id: 3, x: 18, y: 18, d: ObstacleDirection.S },
  ],
};
