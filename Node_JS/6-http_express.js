const express = require("express");
const app = express();
const port = 1245;

app.get("/", function (request, response) {
  response.send("Hello Holberton School!");
});

app.listen(port, function () {
  console.log(`App listening on port ${port}`);
});

module.exports = app;
