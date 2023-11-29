import { useEffect, useState } from "react";
import Navbar from './Navbar.js';
import {Link} from "react-router-dom";
import NewAmenity from './NewAmenity.js'

function Amenities(){
    const [amenities, setAmenities] = useState([]);
  
    useEffect(() => {
      fetch("http://localhost:5555/amenities")
        .then((r) => r.json())
        .then(setAmenities);
    }, []);
  
    function handleAddAmenity(newAmenity) {
      setAmenities((amenities) => [...amenities, newAmenity]);
    }

    return (
      <div>
        <Navbar />
        <h2>Amenities</h2>
        <ul>
          {amenities.map((amenity) => (
            <li key={amenity.id}>
              <span>
                {amenity.name}
              </span>
              <Link to={`/amenities/${amenity.id}`}> View Amenity</Link>
            </li>
          ))}
        </ul>
        <hr />
        <NewAmenity onAddAmenity={handleAddAmenity} />
      </div>
    )
}

export default Amenities