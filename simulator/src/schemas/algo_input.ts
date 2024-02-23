import { Obstacle } from "./obstacle";

export enum AlgoType {
  EXHAUSTIVE_ASTAR = "Exhaustive Astar",
  EUCLIDEAN = "Euclidean",
  BFS = "Breadth First Search",
}

export const AlgoTypeList = [
  AlgoType.EXHAUSTIVE_ASTAR,
  AlgoType.EUCLIDEAN,
  AlgoType.BFS,
];

export interface AlgoInput {
  cat: "obstacles";
  value: {
    obstacles: Obstacle[];
    mode: 0; // 0: Task 1
  };
  server_mode: "simulator";
  algo_type: AlgoType;
}
