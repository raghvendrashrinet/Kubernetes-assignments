const express = require('express');
const app = express();

const PORT = 3000;
const HOST = '0.0.0.0';

let statusMessage = ''; // Store the combined string here

const getHashNow = () => {
  const randomHash = Math.random().toString(36).substring(2, 8);
  const timestamp = new Date().toISOString();
  
  // Combine them together as requested by the assignment
  statusMessage = `${timestamp}: ${randomHash}`;
  
  console.log(statusMessage);
  setTimeout(getHashNow, 5000);
};

getHashNow();

// Serve the statusMessage to the browser
app.get('/', (req, res) => {
  res.send(statusMessage); 
});

app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});