import React from "react";
import {useEffect, useState} from "react"
import {Link} from "react-router-dom"
import Navbar from './Navbar.js'
import Search from "./SearchForm.js"


function Neighborhoods(){

    const [neighborhoods, setNeighborhoods] = useState([])
    const [searchTerm, setSearchTerm] = useState("");

    function getNeighborhoodUrl(){
        fetch("http://127.0.0.1:5555/neighborhoods")
        .then(response => response.json())
        .then(neighborhoodData => setNeighborhoods(neighborhoodData))
    }

    useEffect(getNeighborhoodUrl, []);

    function onSearch(searchString){
        setSearchTerm(searchString)
    };

    const filterNeighborhoods = neighborhoods.filter((neighborhood) => {
        const lowerCaseName = neighborhood.name.toLowerCase();
        const lowerCaseSearchTerm = searchTerm.toLowerCase();
        return lowerCaseName.includes(lowerCaseSearchTerm)
    });

    return (
        <div>
          <Navbar />
          <h2>Neighborhoods</h2>
          <Search onSearch = {onSearch}/>
          <ul>
            {filterNeighborhoods.map((neighborhood) => (
              <li key={neighborhood.id} >
                <span>
                  {neighborhood.name}
                </span>
                <Link to={`/neighborhoods/${neighborhood.id}`}>  View Neighborhood</Link>
              </li>
            ))}
          </ul>
          <hr />
          {/* <NewNeighborhood onAddNeighborhood={handleAddNeighborhood} /> */}
        </div>
      );
    }
    
    export default Neighborhoods;