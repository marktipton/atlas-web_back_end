const http = require('http');
// const fs = require('fs/promises');
const url = require('url');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const app = http.createServer(async (requestObj, responseObj) => {
  const requestUrl = url.parse(requestObj.url, true);
  const { pathname } = requestUrl;
  // console.log(requestUrl);
  // console.log(pathname);

  if (pathname === '/') {
    responseObj.writeHead(200, { 'Content-Type': 'text/plain' });
    responseObj.end('Hello Holberton School!');
  } else if (pathname === '/students') {
    responseObj.writeHead(200, { 'Content-Type': 'text/plain' });

    const databasePath = process.argv[2];
    if (!databasePath) {
      responseObj.end('Database name must be provided as an argument');
      return;
    }
    try {
      // use await bc countstudents is
      // an async operation which returns a promise
      const students = await countStudents(databasePath);
      responseObj.end(`This is the list of our students\n${students}`);
    } catch (error) {
      responseObj.end(`Error: ${error.message}`);
    }
  }
});
app.listen(port, host, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
