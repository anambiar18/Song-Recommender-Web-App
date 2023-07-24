import React, { useState } from 'react';
import axios from 'axios';
import './TextBox.css';

const TextBox = () => {
  const [inputText, setInputText] = useState('');
  const [responseData, setResponseData] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSubmit = () => {
    // Make the API request with the input text
    axios
      .post('/textbox/submit', { text: inputText })
      .then((response) => {
        // Handle the response 
        setResponseData(response.data.response);;
      })
      .catch((error) => {
        // Handle the error 
        console.error(error);
      });

    // Reset the input text
    setInputText('');
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div>
      <input
        type="text"
        value={inputText}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        placeholder="Enter text..."
        className="custom-textbox"
      />
      <button onClick={handleSubmit} className="custom-button">Enter</button>
      <p>{responseData}</p> {/* Render the extracted value instead of the object */}
    </div>
  );
};

export default TextBox;
