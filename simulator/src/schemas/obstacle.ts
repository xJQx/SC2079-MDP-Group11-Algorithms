/** The direction an Obstacle's image is facing */
export enum ObstacleDirection {
  N = "North",
  S = "South",
  E = "East",
  W = "West",
}

/** Obstacle with it's (x, y) co-ordinates and image face direction */
export interface Obstacle {
  x: number;
  y: number;
  direction: ObstacleDirection;
}
