import { useState, useEffect } from 'react';
import SubmitButton from './components/SubmitButton';
import FormGroup from './components/FormGroup';
import Headers from './components/Headers';
// import './style.css'

function App() {
  return (
    <div>
      <h1>Welcome to p-wikiracer!</h1>
      <Headers/>
      <FormGroup/>
      <SubmitButton/>
    </div>
  );
}

export default App;

// function App() {
  
//   const [message, setMessage] = useState('');

//   useEffect(() => {
//     fetch('http://127.0.0.1:5000/api')
//       .then(response => response.json())
//       .then(data => setMessage(data.message));
//   }, []);

//   return (
//     <div>
//       <h1>{message}</h1>
//     </div>
//   );
// }
