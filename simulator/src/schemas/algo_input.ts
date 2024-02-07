import { Obstacle } from "./obstacle";

export interface AlgoInput {
  cat: "obstacles";
  value: {
    obstacles: Obstacle[];
    mode: "simulator";
  };
}
