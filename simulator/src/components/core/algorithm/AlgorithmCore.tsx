import React, { useEffect, useState } from "react";
import { NavigationGrid } from "./NavigationGrid";
import { CoreContainter } from "../CoreContainter";
import { Position } from "../../../schemas/robot";
import {
  ALGO_GRID_BLOCK_SIZE_MULTIPLIER,
  GRID_ANIMATION_SPEED,
  ROBOT_INITIAL_POSITION,
} from "../../../constants";
import {
  FaChevronLeft,
  FaChevronRight,
  FaPause,
  FaPlay,
  FaSitemap,
  FaSpinner,
} from "react-icons/fa";
import { convertAlgoOutputToStepwisePosition } from "./utils/path_animation";
import {
  AlgoTestDataInterface,
  AlgoTestEnum,
  AlgoTestEnumMapper,
} from "../../../tests/algorithm";
import { Button } from "../../common";
import toast from "react-hot-toast";
import { TestSelector } from "./TestSelector";
import { ServerStatus } from "./ServerStatus";
import useFetch from "../../../hooks/useFetch";
import { AlgoInput, AlgoType } from "../../../schemas/algo_input";
import { AlgoOutput } from "../../../schemas/algo_output";
import { AlgorithmSelector } from "./AlgorithmSelector";

export const AlgorithmCore = () => {
  const fetch = useFetch();

  // Robot's Positions
  const [robotPositions, setRobotPositions] = useState<Position[]>();
  const totalSteps = robotPositions?.length ?? 0;

  // Select Algorithm
  const [selectedAlgoTypeEnum, setSelectedAlgoTypeEnum] = useState<AlgoType>(
    AlgoType.EXHAUSTIVE_ASTAR
  );

  // Algorithm Runtime
  const [algoRuntime, setAlgoRuntime] = useState<string>("");

  // Select Tests
  const [selectedTestEnum, setSelectedTestEnum] = useState<AlgoTestEnum>(
    AlgoTestEnum.Basic_Mock
  );
  const [selectedTest, setSelectedTest] = useState<AlgoTestDataInterface>(
    AlgoTestEnumMapper[AlgoTestEnum.Basic_Mock]
  );

  // Select Tests
  useEffect(() => {
    const selectedTest = AlgoTestEnumMapper[selectedTestEnum];
    setSelectedTest(selectedTest);

    setCurrentStep(0);
    setCurrentRobotPosition(ROBOT_INITIAL_POSITION);
    setRobotPositions(undefined);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedTestEnum]);

  // Run Algorithm
  const [isAlgorithmLoading, setIsAlgorithmLoading] = useState(false);

  // Run Algorithm
  const handleRunAlgorithm = async () => {
    if (startAnimation === true || isAlgorithmLoading === true) return;
    setIsAlgorithmLoading(true);
    setAlgoRuntime("");

    const algoInput: AlgoInput = {
      cat: "obstacles",
      value: {
        mode: "simulator",
        obstacles: selectedTest.obstacles.map((o) => {
          return {
            id: o.id,
            x: o.x * ALGO_GRID_BLOCK_SIZE_MULTIPLIER,
            y: o.y * ALGO_GRID_BLOCK_SIZE_MULTIPLIER,
            d: o.d,
          };
        }),
      },
      algo_type: selectedAlgoTypeEnum,
    };
    try {
      const algoOutput: AlgoOutput = await fetch.post(
        "/algo/simulator",
        algoInput
      );
      console.log(algoOutput);
      console.log(convertAlgoOutputToStepwisePosition(algoOutput.positions));
      setRobotPositions(
        convertAlgoOutputToStepwisePosition(algoOutput.positions)
      );
      setCurrentStep(0);

      setAlgoRuntime(algoOutput.runtime);
      toast.success("Algorithm ran successfully.");
    } catch (e) {
      toast.error("Failed to run algorithm. Server Error: " + e);
    }

    setIsAlgorithmLoading(false);
  };

  // Animation
  const [isManualAnimation, setIsManualAnimation] = useState(false);
  const [startAnimation, setStartAnimation] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [currentRobotPosition, setCurrentRobotPosition] = useState<Position>();

  // Animation
  useEffect(() => {
    if (robotPositions && startAnimation && currentStep + 1 < totalSteps) {
      const timer = setTimeout(() => {
        const nextStep = currentStep + 1;
        setCurrentStep(nextStep);

        // Handle Scan Animation
        if (
          robotPositions[nextStep].x === -1 &&
          robotPositions[nextStep].y === -1
        ) {
          if (robotPositions[nextStep].theta === -1)
            toast.success("Image Scanned!");
          else toast("Scanning image...");
        } else {
          setCurrentRobotPosition(robotPositions[nextStep]);
        }

        // Stop Animation at the last step
        if (nextStep === totalSteps - 1) {
          setStartAnimation(false);
        }
      }, GRID_ANIMATION_SPEED);
      return () => clearTimeout(timer);
    } else if (
      robotPositions &&
      isManualAnimation &&
      currentStep < totalSteps
    ) {
      // User manually click through the steps
      // Handle Scan Animation
      if (
        robotPositions[currentStep].x === -1 &&
        robotPositions[currentStep].y === -1
      ) {
        if (robotPositions[currentStep].theta === -1)
          toast.success("Image Scanned!");
        else toast("Scanning image...");
      } else {
        setCurrentRobotPosition(robotPositions[currentStep]);
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentStep, totalSteps, startAnimation, isManualAnimation]);

  return (
    <CoreContainter title="Algorithm Simulator">
      {/* Server Status */}
      <ServerStatus />

      {/* Select Tests */}
      <TestSelector
        selectedTestEnum={selectedTestEnum}
        setSelectedTestEnum={setSelectedTestEnum}
        selectedTest={selectedTest}
        setSelectedTest={setSelectedTest}
        setAlgoRuntime={setAlgoRuntime}
      />

      {/* Select ALgorithm */}
      <AlgorithmSelector
        selectedAlgoTypeEnum={selectedAlgoTypeEnum}
        setSelectedAlgoTypeEnum={setSelectedAlgoTypeEnum}
        setAlgoRuntime={setAlgoRuntime}
        setRobotPositions={setRobotPositions}
      />

      {/* Run Algo */}
      <div className="mb-4 flex justify-center">
        <Button onClick={handleRunAlgorithm}>
          <span>Run Algorithm</span>
          {isAlgorithmLoading ? (
            <FaSpinner className="animate-spin" />
          ) : (
            <FaSitemap className="text-[18px]" />
          )}
        </Button>
      </div>

      {/* Algo Runtime */}
      {algoRuntime && (
        <div className="mb-4 flex justify-center">
          Algorithm Runtime:&nbsp;
          <span className="font-bold">{algoRuntime}</span>&nbsp;(
          {selectedAlgoTypeEnum})
        </div>
      )}

      {/* Animation */}
      {robotPositions && (
        <div className="mt-2 mb-4 flex flex-col justify-center items-center gap-2">
          {/* Start Animation */}
          <Button
            onClick={() => {
              if (startAnimation) {
                // Stop Animation
                setStartAnimation(false);
              } else {
                // Start Animation
                setIsManualAnimation(false);
                setStartAnimation(true);
                if (currentStep === totalSteps - 1) {
                  setCurrentRobotPosition(robotPositions[0]);
                  setCurrentStep(0);
                }
              }
            }}
          >
            <span>{startAnimation ? "Stop Animation" : "Start Animation"}</span>
            {startAnimation ? <FaPause /> : <FaPlay />}
          </Button>

          {/* Slider */}
          <label
            htmlFor="steps-range"
            className="font-bold text-[14px] flex gap-2 items-center"
          >
            <FaChevronLeft
              className="cursor-pointer"
              onClick={() => {
                if (!startAnimation && currentStep - 1 >= 0) {
                  setIsManualAnimation(true);
                  setCurrentStep((prev) => prev - 1);
                }
              }}
            />
            <span>
              Step: {currentStep + 1} / {totalSteps}
            </span>
            <FaChevronRight
              className="cursor-pointer"
              onClick={() => {
                if (!startAnimation && currentStep + 1 < totalSteps) {
                  setIsManualAnimation(true);
                  setCurrentStep((prev) => prev + 1);
                }
              }}
            />
          </label>
          <input
            id="steps-range"
            type="range"
            min={0}
            max={totalSteps - 1}
            value={currentStep}
            onChange={(e) => {
              setCurrentStep(Number(e.target.value));
              setIsManualAnimation(true);
            }}
            onPointerUp={() => setIsManualAnimation(false)}
            step={1}
            className="w-1/2 h-2 bg-orange-900 rounded-lg appearance-none cursor-pointer"
            disabled={startAnimation === true}
          />
        </div>
      )}

      {/* Navigation Grid */}
      <NavigationGrid
        robotPosition={currentRobotPosition ?? ROBOT_INITIAL_POSITION}
        obstacles={selectedTest.obstacles}
      />
    </CoreContainter>
  );
};
