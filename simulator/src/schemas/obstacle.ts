/** The direction an Obstacle's image is facing */
export enum ObstacleDirection {
  N = 1,
  S = 2,
  E = 3,
  W = 4,
}

/** Obstacle with it's (x, y) co-ordinates, image face direction, and id */
export interface Obstacle {
  id: number; // obstacle_id
  x: number; // grid format
  y: number; // grid format
  d: ObstacleDirection; // obstacle face direction
}

export const ObstacleDirectionStringMapping = {
  [ObstacleDirection.N]: "North",
  [ObstacleDirection.S]: "South",
  [ObstacleDirection.E]: "East",
  [ObstacleDirection.W]: "West",
};
