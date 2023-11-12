import { useState, useEffect } from 'react';
import SubmitButton from './components/SubmitButton';
import FormGroup from './components/FormGroup';
import Headers from './components/Headers';
import './style.css'

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