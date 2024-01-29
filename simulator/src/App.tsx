import React from "react";
import { NavigationGrid } from "./components/core";
import { Layout } from "./components/misc";

function App() {
  return (
    <div id="app-container" className="font-poppins">
      <Layout>
        <NavigationGrid />
      </Layout>
    </div>
  );
}

export default App;
