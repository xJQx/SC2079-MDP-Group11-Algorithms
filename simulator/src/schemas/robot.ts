/** Position of Robot on the navigational area */
export interface Position {
  x: number;
  y: number;
  theta: number; // in Radian; 0 = West; 1.37 = North; -1.37 = South;
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
  distance_straight?: number;
  distance_arc?: number;
  theta?: number;
  turn_direction?: TurnDirection;
}
