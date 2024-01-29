/** Position of Robot on the navigational area */
export interface Position {
  x: number;
  y: number;
  theta: number; // in Radian; 0 = West; 1.37 = North; -1.37 = South;
}

/** Simplified direction (instead of theta) that the Robot is facing. */
export enum RobotDirection {
  N = "North",
  S = "South",
  E = "East",
  W = "West",
}

/** Robot's Turn Direction when turning in an arc */
export enum TurnDirection {
  Clockwise = "Clockwise",
  Anticlockwise = "Anti-Clockwise",
}

/** Robot's available Action types */
export enum RobotActionEnum {
  Scan = "Scan",
  MoveStraight = "MoveStraight",
  CurveLeft = "CurveLeft",
  CurveRight = "CurveRight",
  MoveBack = "MoveBack",
}

/** Roboto's Action with distance and theta values */
export interface RobotAction {
  type: RobotActionEnum;
  distance_straight?: number; // in cm
  distance_arc?: number; // in cm
  theta?: number; // in radian
  turn_direction?: TurnDirection;
}
