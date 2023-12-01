import { useState, useEffect } from 'react';
import SubmitButton from './components/SubmitButton';
import FormGroup from './components/FormGroup';
import Headers from './components/Headers';
import Car from './components/Car';

function App() {
  return (
    <div>
      <h1>Welcome to p-wikiracer!</h1>
      <Headers/>
      <FormGroup/>
      <SubmitButton/>
      <Car/>
    </div>
  );
}

export default App;