import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [result, setResult] = useState({});

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/process', { input_text: inputValue });
      setResult(response.data);
    } catch (error) {
      console.error('There was an error processing the input!', error);
    }
  };

  return (
    <div className="App">
      <header className='App-header'>
        Fake News Detector
      </header>
      <div className='input-section'>
        <h2>Enter the news</h2>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder='Type your news here...'
        /><br></br>
        <button onClick={handleSubmit}>Check</button>
        <div className='output'>
          {Object.entries(result).map(([model, prediction]) => (
            <p key={model}>{model}: {prediction}</p>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
