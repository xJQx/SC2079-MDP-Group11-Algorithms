import { RobotDirection, TurnDirection } from "../../../../schemas/robot";

/** Converts a Robot's theta (rotation angle) from positive 2 PI range to [-PI, PI] range */
export const convertPositiveThetaToPostiveNegativeScale = (theta: number) => {
  // (0, -PI)
  if (theta > Math.PI) {
    theta = theta - Math.PI;
    theta = Math.PI - theta;
    theta = -theta;
  }

  return theta;
};

/** Converts a Robot's theta (rotation angle) to a simplified RobotDirection consisting of N, S, E, W */
export const convertThetaToDirection = (theta: number) => {
  // -0.785 to 0.785 -> East
  if (-Math.PI / 4 < theta && theta < Math.PI / 4) {
    return RobotDirection.E;
  }
  // 0.785 to 2.355 -> North
  else if (Math.PI / 4 <= theta && theta <= (3 * Math.PI) / 4) {
    return RobotDirection.N;
  }
  // (2.355 to 3.14) or (-2.355 to -3.14) -> West
  else if (
    ((3 * Math.PI) / 4 < theta && theta <= Math.PI) ||
    (-Math.PI <= theta && theta < (-3 * Math.PI) / 4)
  ) {
    return RobotDirection.W;
  }
  // -2.355 to -0.785 -> South
  else if ((-3 * Math.PI) / 4 <= theta && theta <= -Math.PI / 4) {
    return RobotDirection.S;
  }
  return RobotDirection.N;
};

/**
 * Converts a Robot's theta (rotation angle) when executing a Curve Action to a simplified Final RobotDirection consisting of N, S, E, W
 * @param startRobotDirection RobotDirection
 * @param theata number in radian
 * @param turnDirection TurnDirection: "Clockwise" or "Anticlockwise"
 * */
export const convertThetaRotationToFinalDirection = (
  startRobotDirection: RobotDirection,
  theta: number,
  turnDirection: TurnDirection
) => {
  // 1.57 radian -> 90 Degrees Turn
  // Range: [0.785, 2.355]
  if (0 < theta && theta <= 2.355) {
    switch (startRobotDirection) {
      case RobotDirection.N:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.E;
        else return RobotDirection.W;
      case RobotDirection.E:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.S;
        else return RobotDirection.N;
      case RobotDirection.S:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.W;
        else return RobotDirection.E;
      case RobotDirection.W:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.N;
        else return RobotDirection.S;
    }
  }
  // 3.14 -> 180 Degrees Turn
  // Range: (2.355, 3.925]
  else if (2.355 < theta && theta <= 3.925) {
    switch (startRobotDirection) {
      case RobotDirection.N:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.S;
        else return RobotDirection.S;
      case RobotDirection.E:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.W;
        else return RobotDirection.W;
      case RobotDirection.S:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.N;
        else return RobotDirection.N;
      case RobotDirection.W:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.E;
        else return RobotDirection.E;
    }
  }
  // 4.17 radian -> 270 Degrees Turn
  // Range: (3.925, 5.495]
  else if (3.925 < theta && theta <= 5.495) {
    switch (startRobotDirection) {
      case RobotDirection.N:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.W;
        else return RobotDirection.E;
      case RobotDirection.E:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.N;
        else return RobotDirection.S;
      case RobotDirection.S:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.E;
        else return RobotDirection.W;
      case RobotDirection.W:
        if (turnDirection === TurnDirection.Clockwise) return RobotDirection.S;
        else return RobotDirection.N;
    }
  }

  // default
  return startRobotDirection;
};
