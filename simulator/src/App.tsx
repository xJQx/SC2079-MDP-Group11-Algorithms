import React, { useState } from "react";
import { NavigationGrid } from "./components/core";
import { Layout } from "./components/misc";
import { AppFeatureSelector, AppFeaturesEnum } from "./components/common";

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
        <NavigationGrid />
      </Layout>
    </div>
  );
}

export default App;
