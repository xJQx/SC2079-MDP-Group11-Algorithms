import { AlgoOutputPaths } from "../../schemas/algo_output";
import { Obstacle } from "../../schemas/obstacle";
import { AlgoTestBasicMock } from "./basic_mock";

/** Interface for Algorithm Test Data
 * @param obstacles An array of Obstacles.
 * @param paths Optional. Only used for manually setting paths to test animation. Not used to test the algo.
 */
export interface AlgoTestDataInterface {
  paths?: AlgoOutputPaths["paths"];
  obstacles: Obstacle[];
}

export enum AlgoTestEnum {
  Basic_Mock = "Basic Mock",
  Corners = "Corners (Coming Soon)",
  Obstacles_7 = "7 Obstacles (Coming Soon)",
}

export const AlgoTestEnumsList = [
  AlgoTestEnum.Basic_Mock,
  AlgoTestEnum.Corners,
  AlgoTestEnum.Obstacles_7,
];

export const AlgoTestEnumMapper = {
  [AlgoTestEnum.Basic_Mock]: AlgoTestBasicMock,
  [AlgoTestEnum.Corners]: AlgoTestBasicMock,
  [AlgoTestEnum.Obstacles_7]: AlgoTestBasicMock,
};

// Specific Test Exports
export { AlgoTestBasicMock } from "./basic_mock";
