import React, { useState } from "react";
import { Button, ModalContainer } from "../../common";
import { SiSpeedtest } from "react-icons/si";
import { FaCheckSquare, FaSquare } from "react-icons/fa";
import { AlgoTestEnum, AlgoTestEnumsList } from "../../../tests/algorithm";

interface TestSelectorProps {
  selectedTestEnum: AlgoTestEnum;
  setSelectedTestEnum: React.Dispatch<React.SetStateAction<AlgoTestEnum>>;
}

export const TestSelector = (props: TestSelectorProps) => {
  const { selectedTestEnum, setSelectedTestEnum } = props;

  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div className="mt-2 mb-4 flex justify-center items-center">
      {/* Button */}
      <Button onClick={() => setIsModalOpen(true)}>
        <span>Select Test - {selectedTestEnum}</span>
        <SiSpeedtest className="w-[18px] h-[18px]" />
      </Button>

      {/* Modal */}
      {isModalOpen && (
        <ModalContainer title="Tests" onClose={() => setIsModalOpen(false)}>
          <div className="flex flex-col items-start gap-2">
            {AlgoTestEnumsList.map((algoTest) => (
              <TestItem
                key={algoTest}
                test={algoTest}
                isSelected={algoTest === selectedTestEnum}
                setSelectedTestEnum={setSelectedTestEnum}
                setIsModalOpen={setIsModalOpen}
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
  setIsModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

const TestItem = (props: TestItemProps) => {
  const {
    test,
    isSelected = false,
    setSelectedTestEnum,
    setIsModalOpen,
  } = props;

  return (
    <div
      className="group/test flex gap-2 items-center justify-center cursor-pointer"
      onClick={() => {
        setSelectedTestEnum(test);
        setIsModalOpen(false);
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
