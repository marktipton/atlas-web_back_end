const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', async (request_obj, response_obj) => {
  // const requestUrl = url.parse(request_obj.url, true);
  // const { pathname } = requestUrl;

  const databasePath = process.argv[2];
  if (!databasePath) {
    response_obj.status(400).send(
      'Database name must be provided as an argument',
    );
    return;
  }
  try {
    // use await bc countstudents is
    // an async operation which returns a promise
    const students = await countStudents(databasePath);
    response_obj.send(`This is the list of our students\n${students}`);
  } catch (error) {
    response_obj.status(500).send(`Error: ${error.message}`);
  }
});
app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});

module.exports = app;
