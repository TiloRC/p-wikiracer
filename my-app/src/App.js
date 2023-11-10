import logo from './logo.svg';
import './App.css';
import './index.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';



function App() {

  const [postData, setPostData] = useState(null);
  const [responseData, setResponseData] = useState("none");

  // function myPostFunc() {
  //   // Use axios 
  //   let data = { myValue : "the secrets of the world are unknowm to us"};
  //   // axios.something().then("do stuff" localhost:5000/extnesion)
  //   axios.post("http://172.28.131.72:8080/backend-api", data)
  //     .then(response => {
  //       // Handle the response
  //       setPostData(response.data); // Assuming the response data holds the posted data
  //     })
  //     .catch(error => {
  //       // Handle errors
  //       console.error('Error posting data:', error);
  //     });
  // }

  // const myGetFunc = async () => {
  //   try {
  //     alert("hello0")
  //     //"http://172.28.131.72:8080/"
  //     let response = await axios.get("http://172.28.131.72:8080/backend-api"); // Replace with your API endpoint
  //     alert('hello1')
  //     // Assuming the response.data holds the fetched data
  //     setResponseData(response.data);
  //   } catch (error) {
  //     // Handle error
  //     console.error('Error fetching data:', error);
  //   }
  // };

  async function myGetFunc() {
      
       // Use axios 
       let data = { myValue : "the secrets of the world are unknowm to us"};
       alert('hello from react')
       // axios.something().then("do stuff" localhost:5000/extnesion)
       axios.get("http://172.28.131.72:8080/backend-api")
         .then(response => {
           // Handle the response
           alert('hello1')
          //  alert(response.JSON)
           setResponseData(response); // Assuming the response data holds the posted data
         })
         .catch(error => {
           // Handle errors
           console.error('Error posting data:', error);
         });
     }

  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
{/* front end is 3000, back end is 5000 to call flask api */}

<style>
    @import url('https://fonts.googleapis.com/css2?family=Didact+Gothic&family=Press+Start+2P&display=swap');
</style> 

  <header>
    
    <title>p-wikiracer</title>

      


  </header>

<body>


        <h1 className="main-text" data-toggle="tooltip" data-placement="right" title="My tooltip!" >Wikiracer!</h1>

        <h3>Data: {responseData}</h3>

        {/* <form method="POST" action = "/"> */}
            <div className="headers"> 
                <div className="start-header">
                    <div className="rectangle">Input</div>
                </div>
                <div className="end-header">
                    <div className="rectangle">Output</div>
                </div>   
            </div>

            <div className="form-group">
                <div className="start-field">
                    <input type="text" name="start"/>
                    
                </div>
                <div className="end-field">
                    <input type="text" name = "end"/>
                </div>
            </div>
                
            <div className="form-group">
                <div>
                    <div className="result-dropdown-left">
                        {/* {{rslt_l_0}} */}
                    </div>
                    <div className="result-dropdown-left">
                        {/* {{rslt_l_1}} */}
                    </div>
                    <div className="result-dropdown-left">
                        {/* {{rslt_l_2}} */}
                    </div>
                    <div className="result-dropdown-left">
                        {/* {{rslt_l_3}} */}
                    </div>
                    <div className="result-dropdown-left">
                        {/* {{rslt_l_4}} */}
                    </div>
                </div>

                <div className="result-dropdown-right">
                    {/* {{searches2}} */}
                </div>
            </div>
            <div class = "submit-button">
                <input className="btn" onClick={myGetFunc} type="submit" value="submit"/>
            </div>

            <nav id="navigation"></nav>

            <a href="{{ url_for('static', filename='/car.png') }}" className="dot"><img src="/static/car.png"/></a>

        {/* </form> */}

        

</body>

    </div>
  );
}

export default App;
