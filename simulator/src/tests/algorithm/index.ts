import { Obstacle } from "../../schemas/obstacle";
import { AlgoTestBasicMock } from "./basic_mock";
import { AlgoTestBasicUTurn } from "./basic_u_turn";
import { AlgoTestCorners } from "./corners";
import { AlgoTestCustom } from "./custom";
import { AlgoTestObstacles_5_Basic } from "./obstacles_5";
import { AlgoTestObstacles_7 } from "./obstacles_7";
import { AlgoTestShapes_V } from "./shapes";
import {
  AlgoTestCollisionCheck_A,
  AlgoTestCollisionCheck_B,
  AlgoTestCollisionCheck_C,
} from "./collision_check";
import { AlgoTestOfficialMockLayout } from "./official_mock_layout";

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
  Obstacles_5_Basic = "5 Obstacles (Basic)",
  AlgoTestCollisionCheck_A = "Collision Checking (A)",
  AlgoTestCollisionCheck_B = "Collision Checking (B)",
  AlgoTestCollisionCheck_C = "Collision Checking (C)",
  AlgoTestOfficialMockLayout = "Official Mock Layout",
}

export const AlgoTestEnumsList = [
  AlgoTestEnum.Custom,
  AlgoTestEnum.Basic_Mock,
  AlgoTestEnum.Basic_U_Turn,
  AlgoTestEnum.Corners,
  AlgoTestEnum.Obstacles_7,
  AlgoTestEnum.Shapes_V,
  AlgoTestEnum.Obstacles_5_Basic,
  AlgoTestEnum.AlgoTestCollisionCheck_A,
  AlgoTestEnum.AlgoTestCollisionCheck_B,
  AlgoTestEnum.AlgoTestCollisionCheck_C,
  AlgoTestEnum.AlgoTestOfficialMockLayout,
];

export const AlgoTestEnumMapper = {
  [AlgoTestEnum.Custom]: AlgoTestCustom,
  [AlgoTestEnum.Basic_Mock]: AlgoTestBasicMock,
  [AlgoTestEnum.Basic_U_Turn]: AlgoTestBasicUTurn,
  [AlgoTestEnum.Corners]: AlgoTestCorners,
  [AlgoTestEnum.Obstacles_7]: AlgoTestObstacles_7,
  [AlgoTestEnum.Shapes_V]: AlgoTestShapes_V,
  [AlgoTestEnum.Obstacles_5_Basic]: AlgoTestObstacles_5_Basic,
  [AlgoTestEnum.AlgoTestCollisionCheck_A]: AlgoTestCollisionCheck_A,
  [AlgoTestEnum.AlgoTestCollisionCheck_B]: AlgoTestCollisionCheck_B,
  [AlgoTestEnum.AlgoTestCollisionCheck_C]: AlgoTestCollisionCheck_C,
  [AlgoTestEnum.AlgoTestOfficialMockLayout]: AlgoTestOfficialMockLayout,
};

// Specific Test Exports
export { AlgoTestCustom } from "./custom";
export { AlgoTestBasicMock } from "./basic_mock";
export { AlgoTestBasicUTurn } from "./basic_u_turn";
export { AlgoTestCorners } from "./corners";
export { AlgoTestObstacles_7 } from "./obstacles_7";
export { AlgoTestShapes_V } from "./shapes";
export { AlgoTestObstacles_5_Basic } from "./obstacles_5";
export {
  AlgoTestCollisionCheck_A,
  AlgoTestCollisionCheck_B,
  AlgoTestCollisionCheck_C,
} from "./collision_check";
export { AlgoTestOfficialMockLayout } from "./official_mock_layout";
