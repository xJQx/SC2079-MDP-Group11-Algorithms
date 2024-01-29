import { RobotDirection } from "../../../../schemas/robot";

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
