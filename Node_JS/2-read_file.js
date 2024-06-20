const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    // split data by line and remove empty lines
    const csvLines = data.split('\n').filter((line) => line.trim() !== '');
    // take off first line to isolate student data
    const students = csvLines.slice(1);

    const studentsByField = {
      CS: [],
      SWE: [],
    };

    students.forEach((student) => {
      // split line by commas to isolate types of info
      const row = student.split(',');
      const firstName = row[0].trim();
      const field = row[3].trim();
      if (field === 'CS') {
        studentsByField.CS.push(firstName);
      } else if (field === 'SWE') {
        studentsByField.SWE.push(firstName);
      }
    });

    console.log(`Number of students: ${students.length}`);

    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const len = studentsByField[field].length;
        console.log(`Number of students in ${field}: ${len}. `
          + `List: ${studentsByField[field].join(', ')}`);
      }
    }
  } catch (error) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
