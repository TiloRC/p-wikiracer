import AsyncAutocomplete from './AsyncAutocomplete';
import './components.css'
import React, { useState } from 'react';
import axios from 'axios';

function FormGroup() {
  const [startVal, setStartVal] = useState("");
  const [endVal, setEndVal] = useState("");
  const [pathstr, setpathstr] = useState("");


  function handleClick(startVal, endVal) {

    setpathstr("Finding shortest path...");

    axios.get("http://127.0.0.1:5000/api/alg?startValue=" + startVal + "&endValue=" + endVal)
      .then(response => {
        setpathstr(response.data.path)
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    }
    

  return  (
    <div>
      
    <div class="headers">
      <AsyncAutocomplete title="Start Page" setValue={setStartVal}/>
      <div class="input-separator"></div>
      <AsyncAutocomplete title="End Page" setValue={setEndVal}/>
    </div>

    <div class = "submit-button">
        <input class="btn" type="submit" value="submit" onClick={() => handleClick(startVal, endVal)}/>
    </div>
    <div>
      {pathstr}
    </div>
    </div>
  );


}

export default FormGroup;