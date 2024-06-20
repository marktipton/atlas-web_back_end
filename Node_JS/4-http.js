const http = require('http');

const host = 'localhost';
const port = 1245;

const app = http.createServer((requestObj, responseObj) => {
  responseObj.writeHead(200, { 'Content-Type': 'text/plain' });
  responseObj.end('Hello Holberton School!');
});
app.listen(port, host, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
