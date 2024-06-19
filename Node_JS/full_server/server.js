const express = require('express');
const AppController = require('./controllers/AppController');
const app = express();
const port = 1245;

app.get('/', AppController.getHomepage);

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

module.exports = app;
