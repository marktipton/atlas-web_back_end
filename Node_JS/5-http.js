const http = require('http');
const fs = require('fs/promises');
const url = require('url');
const countStudents = require('./3-read_file_async');
const host = 'localhost';
const port = 1245;

const app = http.createServer(async (request_obj, response_obj) => {
  const requestUrl = url.parse(request_obj.url, true);
  const { pathname } = requestUrl;

  if (pathname === '/') {
    response_obj.writeHead(200, { 'Content-Type': 'text/plain'});
    response_obj.end('Hello Holberton School!');
  } else if (pathname === '/students') {
    response_obj.writeHead(200, { 'Content-Type': 'text/plain' });

    const databasePath = process.argv[2];
    if (!databasePath) {
      response_obj.end('Database name must be provided as an argument');
      return;
    }
  }
});
app.listen(port, host, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
