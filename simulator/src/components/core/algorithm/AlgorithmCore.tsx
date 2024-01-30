import React, { useEffect, useState } from "react";
import { NavigationGrid } from "./NavigationGrid";
import { CoreContainter } from "../CoreContainter";
import { Position } from "../../../schemas/robot";
import {
  GRID_ANIMATION_SPEED,
  ROBOT_INITIAL_POSITION,
} from "../../../constants";
import { FaPlay } from "react-icons/fa";
import { convertPathToStepwisePosition } from "./utils/path_animation";
import {
  AlgoTestDataInterface,
  AlgoTestEnum,
  AlgoTestEnumMapper,
} from "../../../tests/algorithm";
import { Button } from "../../common";
import toast from "react-hot-toast";
import { TestSelector } from "./TestSelector";
import { ServerStatus } from "./ServerStatus";

export const AlgorithmCore = () => {
  // Robot's Positions
  const [robotPositions, setRobotPositions] = useState<Position[]>();
  const totalSteps = robotPositions?.length ?? 0;

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

    if (selectedTest.paths) {
      setRobotPositions(convertPathToStepwisePosition(selectedTest.paths));
    } else {
      // TODO: Fetch Paths from Backend Algorithm
      setRobotPositions([ROBOT_INITIAL_POSITION]);
      setCurrentRobotPosition(ROBOT_INITIAL_POSITION);
      toast.error("Server is offline");
    }
    setCurrentStep(0);
  }, [selectedTestEnum]);

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
      />

      {/* Animation */}
      {robotPositions && (
        <div className="mt-2 mb-4 flex flex-col justify-center items-center gap-2">
          {/* Start Animation */}
          <Button
            onClick={() => {
              setStartAnimation(true);
              setCurrentRobotPosition(robotPositions[0]);
              setCurrentStep(0);
            }}
          >
            <span>Start Animation</span>
            <FaPlay />
          </Button>

          {/* Slider */}
          <label htmlFor="steps-range" className="font-bold text-[14px]">
            Step: {currentStep + 1} / {totalSteps}
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
