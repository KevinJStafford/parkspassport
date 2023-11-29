import { useEffect, useState } from "react";
import { useParams } from "react-router";
import NewPark from './NewPark'
import {Link} from "react-router-dom"

function Parks(){
    const [parks, setParks] = useState([]);
  
    useEffect(() => {
      fetch("http://localhost:5555/parks")
        .then((r) => r.json())
        .then(setParks);
    }, []);
  
    function handleAddPark(newPark) {
      setParks((parks) => [...parks, newPark]);
    }
  
    return (
      <div>
        <h2>Parks</h2>
        <ul>
          {parks.map((park) => (
            <li key={park.id}>
              <span>
                {park.name}, Location {park.location}
              </span>
              <Link to={`/parks/${park.id}`}>View Park</Link>
            </li>
          ))}
        </ul>
        <hr />
        <NewPark onAddPark={handleAddPark} />
      </div>
    );
  }
  
  export default Parks;
