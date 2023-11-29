import React, { useEffect, useState } from "react";
import {Switch, Route } from "react-router-dom";
import LandingGrid from './LandingGrid'
import Navbar from './Navbar'
import Parks from './Park'
import Neighborhoods from './Neighborhood'

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
      </Switch>
    </main>
  );
}

export default App;
