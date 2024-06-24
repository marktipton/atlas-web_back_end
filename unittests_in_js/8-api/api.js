const express = require('express');
const app = express();

const port = 7865;
const host = 'localhost';

app.get('/', (request, response) => {
  response.send('Welcome to the payment system');
});

app.listen(port, () => {
  console.log(`API available on ${host} port ${port}`);
});
