const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
