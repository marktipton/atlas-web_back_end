const http = require('http');

const host = 'localhost';
const port = 1245;

const app = http.createServer((request_obj, response_obj) => {
  response_obj.writeHead(200, { 'Content-Type': 'text/plain' });
  response_obj.end('Hello Holberton School!');
});
app.listen(port, host, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
