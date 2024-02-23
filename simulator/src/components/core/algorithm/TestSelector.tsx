import React, { useState } from "react";
import { Button, ModalContainer } from "../../common";
import { SiSpeedtest } from "react-icons/si";
import {
  FaBox,
  FaCheckSquare,
  FaCircle,
  FaPlus,
  FaSquare,
} from "react-icons/fa";
import { MdDelete } from "react-icons/md";
import {
  AlgoTestDataInterface,
  AlgoTestEnum,
  AlgoTestEnumsList,
} from "../../../tests/algorithm";
import {
  Obstacle,
  ObstacleDirection,
  ObstacleDirectionStringMapping,
} from "../../../schemas/obstacle";
import toast from "react-hot-toast";
import { ROBOT_GRID_HEIGHT, ROBOT_GRID_WIDTH } from "../../../constants";

interface TestSelectorProps {
  selectedTestEnum: AlgoTestEnum;
  setSelectedTestEnum: React.Dispatch<React.SetStateAction<AlgoTestEnum>>;
  selectedTest: AlgoTestDataInterface; // For Managing Custom Obstacles
  setSelectedTest: React.Dispatch<React.SetStateAction<AlgoTestDataInterface>>; // For Managing Custom Obstacles
  setAlgoRuntime: React.Dispatch<string>; // For reseting AlgoRuntime when changing the test
}

export const TestSelector = (props: TestSelectorProps) => {
  const {
    selectedTestEnum,
    setSelectedTestEnum,
    selectedTest,
    setSelectedTest,
    setAlgoRuntime,
  } = props;

  const [isTestModalOpen, setIsTestModalOpen] = useState(false);

  // Custom Obstacle
  const [isManageObstaclesModalOpen, setIsManageObstaclesModalOpen] =
    useState(false);
  const [customObstacle_X, setCustomObstacle_X] = useState<number>(0);
  const [customObstacle_Y, setCustomObstacle_Y] = useState<number>(0);
  const [customObstacle_Direction, setCustomObstacle_Direction] =
    useState<ObstacleDirection>(ObstacleDirection.N);
  const handleAddCustomObstacle = () => {
    // Check that cell is not occupied by Robot
    if (
      0 <= customObstacle_X &&
      customObstacle_X <= ROBOT_GRID_WIDTH - 1 &&
      0 <= customObstacle_Y &&
      customObstacle_Y <= ROBOT_GRID_HEIGHT - 1
    ) {
      return toast.error("Cell is occupied by the Robot!");
    }
    // Check that cell is not occupied by existing Obstacle
    if (
      selectedTest.obstacles.filter(
        (o) => o.x === customObstacle_X && o.y === customObstacle_Y
      ).length > 0
    ) {
      return toast.error("Cell is already occupied by an Obstacle!");
    }

    const updated = {
      obstacles: [
        ...selectedTest.obstacles,
        {
          id: selectedTest.obstacles.length,
          x: customObstacle_X,
          y: customObstacle_Y,
          d: customObstacle_Direction,
        },
      ],
    };
    setSelectedTest(updated);
  };

  return (
    <div className="mt-2 mb-4 flex justify-center items-center gap-2">
      {/* Button */}
      <Button onClick={() => setIsTestModalOpen(true)}>
        <span>Select Test - {selectedTestEnum}</span>
        <SiSpeedtest className="w-[18px] h-[18px]" />
      </Button>

      {/* Manage Custom Obstacles */}
      {selectedTestEnum === AlgoTestEnum.Custom && (
        <Button onClick={() => setIsManageObstaclesModalOpen(true)}>
          <span>Manage Obstacles</span>
          <FaBox />
        </Button>
      )}

      {/* Manage Custom Obstacles Modal */}
      {isManageObstaclesModalOpen && (
        <ModalContainer
          title="Manage Obstacles"
          onClose={() => setIsManageObstaclesModalOpen(false)}
        >
          <div className="flex flex-col justify-center items-start">
            {/* Obstacles List with Delete */}
            {selectedTest.obstacles.map((obstacle) => (
              <CustomObstacleItem
                obstacle={obstacle}
                setSelectedTest={setSelectedTest}
              />
            ))}

            {/* Add Obstacle */}
            <div className="w-full flex flex-col justify-center items-center mt-4">
              {/* Title */}
              <div className="font-bold text-[18px] mb-2">
                - Add Obstacles -
              </div>

              {/* X */}
              <div className="flex gap-2 items-center my-2">
                <label htmlFor="steps-range" className="font-bold">
                  X:{" "}
                </label>
                <input
                  id="steps-range"
                  type="range"
                  min={0}
                  max={19}
                  value={customObstacle_X}
                  onChange={(e) => {
                    setCustomObstacle_X(Number(e.target.value));
                  }}
                  step={1}
                  className="w-full h-2 bg-orange-900 rounded-lg appearance-none cursor-pointer"
                />
                <span className="font-bold">{customObstacle_X}</span>
              </div>

              {/* Y */}
              <div className="flex gap-2 items-center mb-2">
                <label htmlFor="steps-range" className="font-bold">
                  Y:{" "}
                </label>
                <input
                  id="steps-range"
                  type="range"
                  min={0}
                  max={19}
                  value={customObstacle_Y}
                  onChange={(e) => {
                    setCustomObstacle_Y(Number(e.target.value));
                  }}
                  step={1}
                  className="w-full h-2 bg-orange-900 rounded-lg appearance-none cursor-pointer"
                />
                <span className="font-bold">{customObstacle_Y}</span>
              </div>

              {/* Direction */}
              <div className="flex gap-2 items-center mb-4">
                <label className="font-bold">Direction: </label>
                <Button
                  className={`${
                    customObstacle_Direction === ObstacleDirection.N &&
                    "!text-orange-300"
                  }`}
                  onClick={() =>
                    setCustomObstacle_Direction(ObstacleDirection.N)
                  }
                >
                  N
                </Button>
                <Button
                  className={`${
                    customObstacle_Direction === ObstacleDirection.S &&
                    "!text-orange-300"
                  }`}
                  onClick={() =>
                    setCustomObstacle_Direction(ObstacleDirection.S)
                  }
                >
                  S
                </Button>
                <Button
                  className={`${
                    customObstacle_Direction === ObstacleDirection.E &&
                    "!text-orange-300"
                  }`}
                  onClick={() =>
                    setCustomObstacle_Direction(ObstacleDirection.E)
                  }
                >
                  E
                </Button>
                <Button
                  className={`${
                    customObstacle_Direction === ObstacleDirection.W &&
                    "!text-orange-300"
                  }`}
                  onClick={() =>
                    setCustomObstacle_Direction(ObstacleDirection.W)
                  }
                >
                  W
                </Button>
              </div>

              {/* Add Obstacle Button */}
              <Button onClick={handleAddCustomObstacle}>
                <span>Add</span>
                <FaPlus />
              </Button>
            </div>
          </div>
        </ModalContainer>
      )}

      {/* Test Modal */}
      {isTestModalOpen && (
        <ModalContainer title="Tests" onClose={() => setIsTestModalOpen(false)}>
          <div className="flex flex-col items-start gap-2">
            {AlgoTestEnumsList.map((algoTest) => (
              <TestItem
                key={algoTest}
                test={algoTest}
                isSelected={algoTest === selectedTestEnum}
                setSelectedTestEnum={setSelectedTestEnum}
                setIsTestModalOpen={setIsTestModalOpen}
                setAlgoRuntime={setAlgoRuntime}
              />
            ))}
          </div>
        </ModalContainer>
      )}
    </div>
  );
};

interface TestItemProps {
  test: AlgoTestEnum;
  isSelected?: boolean;
  setSelectedTestEnum: React.Dispatch<React.SetStateAction<AlgoTestEnum>>;
  setIsTestModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
  setAlgoRuntime: React.Dispatch<string>; // For reseting AlgoRuntime when changing the test
}

const TestItem = (props: TestItemProps) => {
  const {
    test,
    isSelected = false,
    setSelectedTestEnum,
    setIsTestModalOpen,
    setAlgoRuntime,
  } = props;

  return (
    <div
      className="group/test flex gap-2 items-center justify-center cursor-pointer"
      onClick={() => {
        setSelectedTestEnum(test);
        setIsTestModalOpen(false);
        setAlgoRuntime("");
      }}
    >
      {isSelected ? (
        <FaCheckSquare />
      ) : (
        <>
          <FaCheckSquare className="hidden group-hover/test:inline" />
          <FaSquare className="inline group-hover/test:hidden" />
        </>
      )}
      <div
        className={`${isSelected && "font-bold"} group-hover/test:font-bold`}
      >
        {test}
      </div>
    </div>
  );
};

interface CustomObstacleItemProps {
  obstacle: Obstacle;
  setSelectedTest: React.Dispatch<React.SetStateAction<AlgoTestDataInterface>>;
}

const CustomObstacleItem = (props: CustomObstacleItemProps) => {
  const { setSelectedTest, obstacle } = props;
  const { x, y, d } = obstacle;

  const handleRemoveObstacle = () => {
    setSelectedTest((prev) => {
      const cleanedObstacles = prev.obstacles.filter(
        (o) => !(o.x === obstacle.x && o.y === obstacle.y)
      );

      return {
        obstacles: cleanedObstacles,
      };
    });
  };

  return (
    <div className="flex items-center justify-center gap-2 font-bold">
      <FaCircle className="text-[8px]" />
      <span>X: {x},</span>
      <span>Y: {y},</span>
      <span>Face: {ObstacleDirectionStringMapping[d]}</span>
      <MdDelete
        title="Remove"
        className="text-[20px] hover:text-red-600 cursor-pointer"
        onClick={handleRemoveObstacle}
      />
    </div>
  );
};
