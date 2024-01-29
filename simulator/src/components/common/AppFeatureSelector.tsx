import React, { useState } from "react";
import { FaChevronDown, FaSitemap, FaEye, FaBrain } from "react-icons/fa";

interface AppFeatureSelectorProps {
  selectedFeature: AppFeaturesEnum;
  setSelectedFeature: React.Dispatch<React.SetStateAction<AppFeaturesEnum>>;
}

export const AppFeatureSelector = (props: AppFeatureSelectorProps) => {
  const { selectedFeature, setSelectedFeature } = props;

  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="relative mt-4 flex justify-center">
      <div className="relative min-w-[210px] bg-orange-900 text-white px-2 py-1 rounded shadow-xl">
        {/* Selector */}
        <div
          className="flex items-center justify-between cursor-pointer gap-2"
          onClick={() => setIsOpen((prev) => !prev)}
        >
          {AppFeaturesLogoMap[selectedFeature]}
          <span className="font-bold">{selectedFeature}</span>
          <FaChevronDown
            className={`w-[12px] h-[12px] ${
              isOpen && "rotate-180"
            } transition-all`}
          />
        </div>

        {/* Options */}
        <div
          className={`${
            !isOpen && "invisible translate-y-1"
          } absolute top-10 left-0 flex flex-col gap-3 bg-orange-900 px-2 py-2 rounded w-full cursor-pointer transition-all`}
        >
          {AppFeatures.map((currentFeature) => (
            <AppFeatureSelectorOptions
              key={currentFeature}
              selectedFeature={selectedFeature}
              setSelectedFeature={setSelectedFeature}
              setIsOpen={setIsOpen}
              currentFeature={currentFeature}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

interface AppFeatureSelectorOptionsProps extends AppFeatureSelectorProps {
  setIsOpen: React.Dispatch<React.SetStateAction<boolean>>;
  currentFeature: AppFeaturesEnum;
}

const AppFeatureSelectorOptions = (props: AppFeatureSelectorOptionsProps) => {
  const { selectedFeature, setSelectedFeature, setIsOpen, currentFeature } =
    props;

  return (
    <div
      className={`flex items-center gap-2 hover:text-orange-300 hover:font-bold ${
        selectedFeature === currentFeature && "font-bold text-orange-300"
      }`}
      onClick={() => {
        setIsOpen(false);
        setSelectedFeature(currentFeature);
      }}
    >
      {AppFeaturesLogoMap[currentFeature]}
      <span>{currentFeature}</span>
    </div>
  );
};

// Helpers
export enum AppFeaturesEnum {
  Algorithm = "Algorithm",
  Symbol_Recognition = "Symbol Recognition",
  Rasberry_Pi = "Rasberry Pi",
}
const AppFeatures = [
  AppFeaturesEnum.Algorithm,
  AppFeaturesEnum.Symbol_Recognition,
  AppFeaturesEnum.Rasberry_Pi,
];
const AppFeaturesLogoMap = {
  [AppFeaturesEnum.Algorithm]: <FaSitemap />,
  [AppFeaturesEnum.Symbol_Recognition]: <FaEye />,
  [AppFeaturesEnum.Rasberry_Pi]: <FaBrain />,
};
