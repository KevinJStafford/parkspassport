// import React, { useEffect, useState } from "react";
import {Switch, Route } from "react-router-dom";
import LandingGrid from './LandingGrid'
import Navbar from './Navbar'
import Parks from './Park'
import Neighborhoods from './Neighborhood'
import Amenities from "./Amenity"

function App() {

  return (
    <main>
      <Switch>
        <Route exact path="/">
          <Navbar />
          <LandingGrid />;
      </Route>
      <Route exact path="/parks">
        <Parks />
      </Route>
      <Route exact path="/neighborhoods">
        <Neighborhoods/>
      </Route>
      <Route exact path="/amenities">
        <Amenities />
      </Route>
      </Switch>
    </main>
  );
}

export default App;
