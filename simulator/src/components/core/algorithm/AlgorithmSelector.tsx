import React, { useState } from "react";
import { Button, ModalContainer } from "../../common";
import { FaCheckSquare, FaSitemap, FaSquare } from "react-icons/fa";
import { AlgoType, AlgoTypeList } from "../../../schemas/algo_input";

interface AlgorithmSelectorProps {
  selectedAlgoTypeEnum: AlgoType;
  setSelectedAlgoTypeEnum: React.Dispatch<React.SetStateAction<AlgoType>>;
}

export const AlgorithmSelector = (props: AlgorithmSelectorProps) => {
  const { selectedAlgoTypeEnum, setSelectedAlgoTypeEnum } = props;

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
}

const AlgorithmSelectorItem = (props: AlgorithmSelectorItemProps) => {
  const {
    test,
    isSelected = false,
    setSelectedAlgoTypeEnum,
    setIsAlgorithmSelectorModalOpen,
  } = props;

  return (
    <div
      className="group/test flex gap-2 items-center justify-center cursor-pointer"
      onClick={() => {
        setSelectedAlgoTypeEnum(test);
        setIsAlgorithmSelectorModalOpen(false);
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
