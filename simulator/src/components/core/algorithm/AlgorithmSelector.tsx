import React, { useState } from "react";
import { Button, ModalContainer } from "../../common";
import { FaCheckSquare, FaSitemap, FaSquare } from "react-icons/fa";
import { AlgoType, AlgoTypeList } from "../../../schemas/algo_input";
import { Position } from "../../../schemas/robot";

interface AlgorithmSelectorProps {
  selectedAlgoTypeEnum: AlgoType;
  setSelectedAlgoTypeEnum: React.Dispatch<React.SetStateAction<AlgoType>>;
  setAlgoRuntime: React.Dispatch<string>;
  setRobotPositions: React.Dispatch<
    React.SetStateAction<Position[] | undefined>
  >;
}

export const AlgorithmSelector = (props: AlgorithmSelectorProps) => {
  const {
    selectedAlgoTypeEnum,
    setSelectedAlgoTypeEnum,
    setAlgoRuntime,
    setRobotPositions,
  } = props;

  const [isAlgorithmSelectorModalOpen, setIsAlgorithmSelectorModalOpen] =
    useState(false);

  return (
    <div className="mt-2 mb-4 flex justify-center items-center gap-2">
      {/* Button */}
      <Button onClick={() => setIsAlgorithmSelectorModalOpen(true)}>
        <span>Select Algorithm - {selectedAlgoTypeEnum}</span>
        <FaSitemap className="w-[18px] h-[18px]" />
      </Button>

      {/* Algorithm Selector Modal */}
      {isAlgorithmSelectorModalOpen && (
        <ModalContainer
          title="Algorithms"
          onClose={() => setIsAlgorithmSelectorModalOpen(false)}
        >
          <div className="flex flex-col items-start gap-2">
            {AlgoTypeList.map((algoTest) => (
              <AlgorithmSelectorItem
                key={algoTest}
                test={algoTest}
                isSelected={algoTest === selectedAlgoTypeEnum}
                setSelectedAlgoTypeEnum={setSelectedAlgoTypeEnum}
                setIsAlgorithmSelectorModalOpen={
                  setIsAlgorithmSelectorModalOpen
                }
                setAlgoRuntime={setAlgoRuntime}
                setRobotPositions={setRobotPositions}
              />
            ))}
          </div>
        </ModalContainer>
      )}
    </div>
  );
};

interface AlgorithmSelectorItemProps {
  test: AlgoType;
  isSelected?: boolean;
  setSelectedAlgoTypeEnum: React.Dispatch<React.SetStateAction<AlgoType>>;
  setIsAlgorithmSelectorModalOpen: React.Dispatch<
    React.SetStateAction<boolean>
  >;
  setAlgoRuntime: React.Dispatch<string>;
  setRobotPositions: React.Dispatch<
    React.SetStateAction<Position[] | undefined>
  >;
}

const AlgorithmSelectorItem = (props: AlgorithmSelectorItemProps) => {
  const {
    test,
    isSelected = false,
    setSelectedAlgoTypeEnum,
    setIsAlgorithmSelectorModalOpen,
    setAlgoRuntime,
    setRobotPositions,
  } = props;

  return (
    <div
      className="group/test flex gap-2 items-center justify-center cursor-pointer"
      onClick={() => {
        setSelectedAlgoTypeEnum(test);
        setIsAlgorithmSelectorModalOpen(false);
        setAlgoRuntime("");
        setRobotPositions(undefined);
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
