from arena.map import Map
from arena.obstacle import Obstacle

from common.consts import SNAP_COORD
from common.types import Position
from common.utils import _mappings as Int_to_Direction_mappings

from math import pi

from path_finding.hamiltonian_path import ExhaustiveSearch

from robot.stm_commands import convert_segments_to_commands

import multiprocessing as mp

""" -------------------------------------- """
""" ---------- Endpoint Schemas ---------- """
""" -------------------------------------- """
from pydantic import BaseModel
from enum import Enum

# Input
class AlgoInputMode(Enum):
  SIMULATOR = "simulator"
  LIVE = "live"

class AlgoInputValueObstacle(BaseModel):
  id: int # obstacle_id
  x: int # grid_format
  y: int # grid_format
  d: int # direction of obstacle; 1: North; 2: South; 3: East; 4: West

class AlgoInputValue(BaseModel):
  obstacles: list[AlgoInputValueObstacle]
  mode: AlgoInputMode

class AlgoInput(BaseModel):
  cat: str = "obstacle"
  value: AlgoInputValue

# Output
class AlgoOutputSimulatorPosition(BaseModel):
  x: int # in cm
  y: int # in cm
  theta: float # in radian

class AlgoOutputSimulator(BaseModel):
  positions: list[AlgoOutputSimulatorPosition]


""" -------------------------------------- """
""" ----------- Main Functions ----------- """
""" -------------------------------------- """
if __name__ == '__main__':
  mp.freeze_support() # Needed to run child processes (multiprocessing)

def main(algo_input: AlgoInput):
  # Algorithm Mode -> 'simulator' or 'live'
  algo_mode = algo_input["value"]["mode"]

  # Obstacles
  obstacles = _extract_obstacles_from_input(algo_input["value"]["obstacles"])

  # Start Position
  start_position = Position(x=0, y=0, theta=pi/2)

  # Map
  map = Map(obstacles=obstacles)

  # Algorithm
  algo = ExhaustiveSearch(map=map, src=start_position)

  # Algorithm Search⭐
  min_perm, paths = algo.search()

  # Results
  if algo_mode == AlgoInputMode.SIMULATOR:
    simulator_algo_output = [] # Array of positions
    for path in paths:
      for node in path:
        simulator_algo_output.append(node.pos)
      
      # Position configuration to represent scanning (*only for simulator)
      simulator_algo_output.append(Position(-1, -1, -2)) 
      simulator_algo_output.append(Position(-1, -1, -1)) 

    return simulator_algo_output
  
  # TODO: STM Commands for `live` mode
  if algo_mode == AlgoInputMode.LIVE:
    for path in paths:
      print("\t-----stm commands-----")
      stm_commands = convert_segments_to_commands(path)
      print(stm_commands)

def _extract_obstacles_from_input(input_obstacles):
  """
  Helper function to convert input obstacles to `Obstacle` object accepted by the algorithm
  """
  obstacles = []

  for obstacle in input_obstacles:
    obstacles.append(Obstacle(
      x=obstacle["x"] * SNAP_COORD,
      y=obstacle["y"] * SNAP_COORD,
      facing=Int_to_Direction_mappings[str(obstacle["d"])]
    ))

  return obstacles


""" -------------------------------------- """
""" ------ FastAPI (API Endpoints) ------- """
""" -------------------------------------- """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
  return { "message": "Hello World" }

@app.get("/algo/simulator/simple-test", tags=["Algorithm"])
async def algo_simulator_test():
  """To test algo and endpoint on the server without starting up the web simulator"""
  # Basic Mock Data
  simulator_algo_input: AlgoInput = {
    "cat": "obstacles",
    "value": {
      "obstacles": [
        { "id": 1, "x": 30, "y": 20, "d": 4 },
        { "id": 2, "x": 2, "y": 36, "d": 2 },
      ],
      "mode": AlgoInputMode.SIMULATOR
    }
  }
  positions = main(simulator_algo_input)
  
  return { "positions": positions }

@app.post("/algo/simulator", response_model=AlgoOutputSimulator, tags=["Algorithm"])
async def algo_simulator(algo_input: AlgoInput):
  """Main endpoint for simulator"""
  positions = main(algo_input.model_dump())

  return { "positions": positions }

# TODO: Create Endpoint for `live` mode