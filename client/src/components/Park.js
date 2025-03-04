import { useEffect, useState } from "react";
import Navbar from './Navbar.js';
// import {Link} from "react-router-dom";
import Search from "./SearchForm.js"
// import { FaTrashCan } from "react-icons/fa6";


function Parks(){
    const [parks, setParks] = useState([]);
    const [searchTerm, setSearchTerm] = useState("");
  
    useEffect(() => {
      fetch("http://localhost:5555/parks")
        .then((r) => r.json())
        .then(setParks);
    }, []);
  
    // Not in MVP
    // function handleAddPark(newPark) {
    //   setParks((parks) => [...parks, newPark]);
    // };

    function onSearch(searchString){
      setSearchTerm(searchString)
    };

    const filterParks = parks.filter((park) => {
      const lowerCaseName = park.name.toLowerCase();
      const lowerCaseSearchTerm = searchTerm.toLowerCase();
      return lowerCaseName.includes(lowerCaseSearchTerm)
    });

    // function handleDelete(id){
    //   fetch(`/parks/${id}`, {method: "DELETE",}).then((r) => {
    //     if (r.ok) {
    //       setParks((parks) =>
    //       parks.filter((park) => park.id !== id)
    //       );
    //     }
    //   }); 
    // };
 
    return (
      <div>
        <Navbar />
        <h2>Parks</h2>
        <Search onSearch = {onSearch}/>
        <ul>
          {filterParks.map((park) => (
            <li key={park.id}>
              <span>
                {park.name},  Location:  {park.location} 
              </span>
              {/* <Link to={`/parks/${park.id}`}> View Park</Link> */}
              {/* removed delete because there is no way to add parks */}
              {/* <FaTrashCan onClick={() => handleDelete(park.id)}/>  */} 
            </li>
          ))}
        </ul>
        <hr />
      </div>
    );
  }
  
  export default Parks;
