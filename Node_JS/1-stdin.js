let str = "Welcome to Holberton School, what is your name?";

console.log(str);
process.stdin.on('data', data => {
  // process.stdin.read();
  process.stdout.write(`Your name is: ${data.toString()}`);
  // console
  // process.exit();
});
