import React, { useEffect, useState } from "react";
import { NavigationGrid } from "./NavigationGrid";
import { CoreContainter } from "../CoreContainter";
import { Position } from "../../../schemas/robot";
import { GRID_ANIMATION_SPEED } from "../../../constants";
import { FaPlay } from "react-icons/fa";
import { convertPathToStepwisePosition } from "./utils/path_animation";
import { AlgoTestBasicMock } from "../../../tests/algorithm";
import { Button } from "../../common";

export const AlgorithmCore = () => {
  // Mock Data -> To Remove
  const paths = AlgoTestBasicMock.paths;
  const obstacles = AlgoTestBasicMock.obstacles;

  const robotPositions: Position[] = convertPathToStepwisePosition(paths);
  const totalSteps = robotPositions.length;

  const [startAnimation, setStartAnimation] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [currentRobotPosition, setCurrentRobotPosition] = useState<Position>(
    robotPositions[0]
  );

  // Animation
  useEffect(() => {
    if (startAnimation && currentStep + 1 < totalSteps) {
      const timer = setTimeout(() => {
        const nextStep = currentStep + 1;
        setCurrentStep(nextStep);
        setCurrentRobotPosition(robotPositions[nextStep]);

        if (nextStep === totalSteps - 1) {
          setStartAnimation(false);
        }
      }, GRID_ANIMATION_SPEED);
      return () => clearTimeout(timer);
    } else if (currentStep < totalSteps) {
      // User manually click through the steps
      setCurrentRobotPosition(robotPositions[currentStep]);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentStep, totalSteps, startAnimation]);

  return (
    <CoreContainter title="Algorithm Simulator">
      {/* Animation */}
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
          onChange={(e) => setCurrentStep(Number(e.target.value))}
          step={1}
          className="w-1/2 h-2 bg-orange-900 rounded-lg appearance-none cursor-pointer"
          disabled={startAnimation === true}
        />
      </div>

      {/* Navigation Grid */}
      <NavigationGrid
        robotPosition={currentRobotPosition}
        obstacles={obstacles}
      />
    </CoreContainter>
  );
};
