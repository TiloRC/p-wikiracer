import AsyncAutocomplete from './AsyncAutocomplete';
import './components.css'
import React, { useState } from 'react';

function FormGroup() {
  const [startVal, setStartVal] = useState("");
  const [endVal, setEndVal] = useState("");
  const [pathstr, setpathstr] = useState("");


  function handleClick(inputText, outputText) {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ inputtext: startVal,
                              outputtext: endVal})
    };
    fetch('http://127.0.0.1:5000/api/alg', requestOptions)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const response_value = response.json();
        response_value
          .then((value) => {
            console.log(value);
            setpathstr(value);
          })
        console.log(response_value);
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
        <div>
          {startVal}
          {endVal}
          {pathstr}
        </div>
      </div>
    </div>
  );

}

export default FormGroup;