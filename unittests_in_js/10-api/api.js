const express = require('express');
const app = express();
app.use(express.json()); // for parsing json bodies

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

app.get('/available_payments', (request, response) => {
  const payments = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };
  response.json(payments);
});

app.post('/login', (request, response) => {
  const { userName } = request.body;
  if (!userName) {
    return response.status(400).send('Missing userName');
  }
  return response.send(`Welcome ${userName}`);
});
app.listen(port, () => {
  console.log(`API available on ${host} port ${port}`);
});

module.exports = app;
