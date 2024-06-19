const express = require("express");
const countStudents = require("./3-read_file_async");
const app = express();
const port = 1245;

app.get("/", function (request, response) {
  response.send("Hello Holberton School!");
});

app.get("/students", async function (request_obj, response_obj) {
  // const requestUrl = url.parse(request_obj.url, true);
  // const { pathname } = requestUrl;

  // if (pathname === '/') {
  //   response_obj.writeHead(200, { 'Content-Type': 'text/plain'});
  //   response_obj.end('Hello Holberton School!');
  // } else if (pathname === '/students') {
  //   response_obj.writeHead(200, { 'Content-Type': 'text/plain' });

  //   const databasePath = process.argv[2];
  //   if (!databasePath) {
  //     response_obj.end('Database name must be provided as an argument');
  //     return;
  //   }
  //   try {
  //     // use await bc countstudents is
  //     // an async operation which returns a promise
  //     const students = await countStudents(databasePath);
  //     response_obj.end(`This is the list of our students\n${students}`);
  //   } catch (error) {
  //     response_obj.end(`Error: ${error.message}`);
  //   }
  // }
});
app.listen(port, function () {
  console.log(`App listening on port ${port}`);
});

module.exports = app;
