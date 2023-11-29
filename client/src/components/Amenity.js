import { useEffect, useState } from "react";
import Navbar from './Navbar.js';
import {Link} from "react-router-dom";
import NewAmenity from './NewAmenity.js'
// import Search from "./SearchForm.js"

function Amenities(){
    const [amenities, setAmenities] = useState([]);
    // const [searchTerm, setSearchTerm] = useState("");
  
    useEffect(() => {
      fetch("http://localhost:5555/amenities")
        .then((r) => r.json())
        .then(setAmenities);
    }, []);
  
    function handleAddAmenity(newAmenity) {
      setAmenities((amenities) => [...amenities, newAmenity]);
    }

    // function onSearch(searchString){
    //   setSearchTerm(searchString)
    // };

    // const filterAmenities = amenities.filter((amenity) => {
    //   const lowerCaseName = amenity.name.toLowerCase();
    //   const lowerCaseSearchTerm = searchTerm.toLowerCase();
    //   return lowerCaseName.includes(lowerCaseSearchTerm)
    // });

    return (
      <div>
        <Navbar />
        <h2>Amenities</h2>
        {/* <Search onSearch = {onSearch}/> */}
        <ul>
          {amenities.map((amenity) => (
            <li key={amenity.id}>
              <span>
                {amenity.amenity_items}
              </span>
              <Link to={`/amenities/${amenity.id}`}> View Amenity</Link>
            </li>
          ))}
        </ul>
        <hr />
        {/* <NewAmenity onAddAmenity={handleAddAmenity} /> */}
      </div>
    )
}

export default Amenities