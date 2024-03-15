import { AlgoTestDataInterface } from ".";
import { ObstacleDirection } from "../../schemas/obstacle";

export const AlgoTestOfficialMockLayout: AlgoTestDataInterface = {
  obstacles: [
    { id: 1, x: 5, y: 9, d: ObstacleDirection.S },
    { id: 2, x: 8, y: 14, d: ObstacleDirection.W },
    { id: 3, x: 12, y: 9, d: ObstacleDirection.E },
    { id: 4, x: 15, y: 4, d: ObstacleDirection.W },
    { id: 5, x: 15, y: 15, d: ObstacleDirection.S },
  ],
};
