import React from "react"


function Search({searchTerm, onSearch}) {
    
    function handleSearch(event){
        onSearch(event.target.value)
        console.log(event.target.value)
    }

    return (
        <div>
            <input type = "text"
            placeholder = "Search..."
            onChange = {handleSearch}
            value = {searchTerm}
            />
            <button type="submit">🔍</button>
        </div>
    );
};

export default Search;

 