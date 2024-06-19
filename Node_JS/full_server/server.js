const express = require('express');
const AppController = require('./controllers/AppController');
const app = express();
const port = 1245;
const router = require('./routes/index');

app.use('/', router);

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

module.exports = app;
