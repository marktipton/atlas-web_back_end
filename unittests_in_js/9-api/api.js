const express = require('express');
const app = express();

const port = 7865;
const host = 'localhost';

app.get('/', (request, response) => {
  response.send('Welcome to the payment system');
});

app.get('/cart/:id', (request, response) => {
  const { id } = request.params;
  if (isNaN(id)) {
    return response.status(404).send('Id must be a number');
  }
  return response.send(`Payment methods for cart ${id}`);
});

app.listen(port, () => {
  console.log(`API available on ${host} port ${port}`);
});

module.exports = app;
