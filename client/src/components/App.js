import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import LandingGrid from './LandingGrid'
import Navbar from './Navbar'

function App() {
  return (
    <div>
      <Navbar />
      <LandingGrid />;
    </div>
  )
}

export default App;
