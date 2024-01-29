import React, { useState } from "react";
import { Layout } from "./components/misc";
import { AppFeatureSelector, AppFeaturesEnum } from "./components/common";
import { AlgorithmCore } from "./components/core/algorithm";
import { SymbolRecognitionCore } from "./components/core/symbol_recognition";
import { RasberryPiCore } from "./components/core/rasberry_pi";

function App() {
  const [selectedFeature, setSelectedFeature] = useState<AppFeaturesEnum>(
    AppFeaturesEnum.Algorithm
  );

  return (
    <div id="app-container" className="font-poppins">
      <Layout>
        <AppFeatureSelector
          selectedFeature={selectedFeature}
          setSelectedFeature={setSelectedFeature}
        />

        {/* Feature-specific Content */}
        {selectedFeature === AppFeaturesEnum.Algorithm && <AlgorithmCore />}
        {selectedFeature === AppFeaturesEnum.Symbol_Recognition && (
          <SymbolRecognitionCore />
        )}
        {selectedFeature === AppFeaturesEnum.Rasberry_Pi && <RasberryPiCore />}
      </Layout>
    </div>
  );
}

export default App;
