const express = require('express');
const app = express();

const PORT = 3000;
const HOST = '0.0.0.0'; // Essential for Kubernetes network routing

let currentHash = '';

// This generates a new hash every 5 seconds and logs it (your original logic)
const generateHashLoop = () => {
  currentHash = Math.random().toString(36).substring(2, 8);
  console.log(currentHash);
  setTimeout(generateHashLoop, 5000);
};
generateHashLoop();

// This endpoint answers HTTP requests sent to http://localhost:8081/
app.get('/', (req, res) => {
  res.send(`Current Hash: ${currentHash}`);
});

// Start the HTTP server on port 3000
app.listen(PORT, HOST, () => {
  console.log(`Server is running and listening on http://${HOST}:${PORT}`);
});