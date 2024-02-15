# Algorithm Server (Python)

**Table of Contents**

- [Algorithm Server (Python)](#algorithm-server-python)
- [Setup Instructions](#setup-instructions)
- [Quick Dive into the Repo](#quick-dive-into-the-repo)
  - [Directories](#directories)
  - [Where to start?](#where-to-start)
  - [Connection Protocol - FastAPI (HTTPS)](#connection-protocol---fastapi-https)
    - [Input Schema](#input-schema)
    - [Output Schema](#output-schema)

# Setup Instructions

1. In the `/algorithms` directory, create a python virtual environment and activate it.

```bash
python -m venv .venv
. .venv/Scripts/activate # The .venv activation command might differ depending on your operating system
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

1. In the same directory (`/algorithms`), start the application.

```bash
uvicorn main:app --reload
```

And you are ready to start using the Algorithm Server! The server application is running on http://127.0.0.1:8000/.

To view the API Endpoint Docs, go to http://127.0.0.1:8000/docs.

**Script for quick startup:**

```bash
cd algorithms
. .venv/Scripts/activate
uvicorn main:app --reload
```

# Quick Dive into the Repo

## Directories

- `📁 arena/`: Defines the `Map` and `Obstacle` class and configure anything related to the navigational area.
- `📁 common/`: Contains commonly used variables and functions. E.g.: `constants`, `enums`, `types`, and `utils`.
- `📁 path_finding/`: The main algorithm related code can be found here!⭐
- `📁 robot/`: Defines the Robot's `moves` and `stm_commands` required to be interpretated by the Robot.
- `📁 simulator/`: Contains the python version of the simulator (Not used).
- `📁 tests/`: Contains python tests to test specific functionality

👉🏻 Entry Point: `main.py`

This is where the app creates an instance of the algorithm and search for the shortest hamiltonian path based on the input obstacles.

## Where to start?

1. Take a quick glance at the `📁 common/` directory's `consts.py`, `enums.py`, `types.py`, and `utils.py` to have a generic understanding of the app (except the algo).
2. Read and understand `path_finding/astar.py`.
   1. Note the output of the `search()` method.
3. Read and understand `path_finding/path_validation.py`.
4. Read and understand `path_finding/hamiltonian_path.py`.
   1. This class calls the Astar search method defined in the `astar.py`.
   2. Likewise, note the output of the `search()` method of this class.
5. [Optional] Read and understand `path_finding/dubins_path.py` (will not be used as the main algo due to the robot's actual curve not being a perfect circle).
6. Read `robot/stm_commands.py` to understand how the algorithm outputs are converted into stm commands.
   1. You might need to modify the `convert_segments_to_commands()` method if your schema defined by the STM / Robot is different.
7. Read `main.py`'s `main` method to see how everything ties together.

## Connection Protocol - FastAPI (HTTPS)

This Algorithm Repo uses FASTAPI and HTTPS + JSON protocol to transmit infomation to/fro the simulator/robot.

### Input Schema

```javascript
{
  cat: "obstacles",
  value: {
    obstacles: {
      id: int,        // obstacle_id
      x: int,         // in grid format
      y: int,         // in grid format
      d: int,         // direction of obstacle; 1: North; 2: South; 3: East; 4: West
    }[],
    mode: "simulator" | "live",
  },
}
```

### Output Schema

```javascript
{
  positions: {
    x: int,         // in cm
    y: int,         // in cm
    theta: float    // in radian
  }
}
```
