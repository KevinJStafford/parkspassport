import React from "react";
import {useEffect, useState} from "react"
import {Link} from "react-router-dom"

function Neighborhoods(){

    const [neighborhoods, setNeighborhoods] = useState([])

    useEffect(() => {
        fetch("http://127.0.0.1:5555/neighborhoods")
        .then((r) => r.json())
        .then(setNeighborhoods);
    }, [])

    return (
        <div>
          <h2>Neighborhoods</h2>
          <ul>
            {neighborhoods.map((neighborhood) => (
              <li key={neighborhood.id}>
                <span>
                  {neighborhood.name}
                </span>
                <Link to={`/neighborhoods/${neighborhood.id}`}>  View Neighborhood</Link>
              </li>
            ))}
          </ul>
          <hr />
          {/* <NewPark onAddPark={handleAddPark} /> */}
        </div>
      );
    }
    
    export default Neighborhoods;