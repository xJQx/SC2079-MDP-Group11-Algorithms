import { AlgoTestDataInterface } from ".";
import { AlgoOutputPaths } from "../../schemas/algo_output";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";
import { RobotActionEnum, TurnDirection } from "../../schemas/robot";

const paths: AlgoOutputPaths["paths"] = [
  {
    startPosition: { x: 0, y: 0, theta: Math.PI / 2 },
    endPosition: { x: 0, y: 13, theta: Math.PI / 2 },
    steps: [
      {
        type: RobotActionEnum.MoveStraight,
        distance_straight: 130,
      },
      {
        type: RobotActionEnum.Scan,
      },
    ],
  },
  {
    startPosition: { x: 0, y: 13, theta: Math.PI / 2 },
    endPosition: { x: 0, y: 13, theta: Math.PI / 2 },
    steps: [
      {
        type: RobotActionEnum.MoveBack,
        distance_straight: 10,
      },
      {
        type: RobotActionEnum.CurveRight,
        distance_arc: 20,
        theta: Math.PI,
        turn_direction: TurnDirection.Clockwise,
      },
      {
        type: RobotActionEnum.CurveLeft,
        distance_arc: 20,
        theta: Math.PI / 2,
        turn_direction: TurnDirection.Anticlockwise,
      },
      {
        type: RobotActionEnum.MoveStraight,
        distance_straight: 10,
      },
      {
        type: RobotActionEnum.Scan,
      },
    ],
  },
];

const obstacles: Obstacle[] = [
  { id: 1, x: 15, y: 10, d: ObstacleDirection.W },
  { id: 2, x: 1, y: 18, d: ObstacleDirection.S },
];

export const AlgoTestBasicMock: AlgoTestDataInterface = {
  paths: paths,
  obstacles: obstacles,
};
