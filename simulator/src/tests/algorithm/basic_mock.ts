import { AlgoOutputPaths } from "../../schemas/algo_output";
import { Obstacle, ObstacleDirection } from "../../schemas/obstacle";
import { RobotActionEnum } from "../../schemas/robot";

const paths: AlgoOutputPaths["paths"] = [
  {
    startPosition: { x: 0, y: 0, theta: Math.PI / 2 },
    endPosition: { x: 0, y: 13, theta: Math.PI / 2 },
    steps: [
      {
        type: RobotActionEnum.MoveStraight,
        distance_straight: 130,
      },
      // {
      //   type: RobotActionEnum.Scan,
      // },
    ],
  },
  // {
  //   startPosition: { x: 0, y: 13, theta: Math.PI / 2 },
  //   endPosition: { x: 0, y: 13, theta: Math.PI / 2 },
  //   steps: [
  //     {
  //       type: RobotActionEnum.MoveBack,
  //       distance_straight: 10,
  //     },
  //     {
  //       type: RobotActionEnum.CurveRight,
  //       distance_arc: 20,
  //       theta: Math.PI,
  //       turn_direction: TurnDirection.Clockwise,
  //     },
  //     {
  //       type: RobotActionEnum.Scan,
  //     },
  //   ],
  // },
];

const obstacles: Obstacle[] = [
  { x: 10, y: 10, direction: ObstacleDirection.W },
  { x: 1, y: 18, direction: ObstacleDirection.S },
];

export const AlgoTestBasicMock = {
  paths: paths,
  obstacles: obstacles,
};