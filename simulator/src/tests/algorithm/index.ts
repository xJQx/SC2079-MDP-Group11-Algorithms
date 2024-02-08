import { Obstacle } from "../../schemas/obstacle";
import { AlgoTestBasicMock } from "./basic_mock";
import { AlgoTestBasicUTurn } from "./basic_u_turn";
import { AlgoTestCorners } from "./corners";
import { AlgoTestCustom } from "./custom";
import { AlgoTestObstacles_7 } from "./obstacles_7";
import { AlgoTestShapes_V } from "./shapes";

/** Interface for Algorithm Test Data
 * @param obstacles An array of Obstacles.
 */
export interface AlgoTestDataInterface {
  obstacles: Obstacle[];
}

export enum AlgoTestEnum {
  Custom = "Custom",
  Basic_Mock = "Basic Mock",
  Basic_U_Turn = "Basic U-Turn",
  Corners = "Corners",
  Obstacles_7 = "7 Obstacles",
  Shapes_V = "V Shape",
}

export const AlgoTestEnumsList = [
  AlgoTestEnum.Custom,
  AlgoTestEnum.Basic_Mock,
  AlgoTestEnum.Basic_U_Turn,
  AlgoTestEnum.Corners,
  AlgoTestEnum.Obstacles_7,
  AlgoTestEnum.Shapes_V,
];

export const AlgoTestEnumMapper = {
  [AlgoTestEnum.Custom]: AlgoTestCustom,
  [AlgoTestEnum.Basic_Mock]: AlgoTestBasicMock,
  [AlgoTestEnum.Basic_U_Turn]: AlgoTestBasicUTurn,
  [AlgoTestEnum.Corners]: AlgoTestCorners,
  [AlgoTestEnum.Obstacles_7]: AlgoTestObstacles_7,
  [AlgoTestEnum.Shapes_V]: AlgoTestShapes_V,
};

// Specific Test Exports
export { AlgoTestCustom } from "./custom";
export { AlgoTestBasicMock } from "./basic_mock";
export { AlgoTestBasicUTurn } from "./basic_u_turn";
export { AlgoTestCorners } from "./corners";
export { AlgoTestObstacles_7 } from "./obstacles_7";
export { AlgoTestShapes_V } from "./shapes";
