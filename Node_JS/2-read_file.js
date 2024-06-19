const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    // split data by line and remove empty lines
    const csv_lines = data.split('\n').filter(line => line.trim() !== '');
    // take off first line to isolate student data
    const students = csv_lines.slice(1);

    const students_by_field = {
      CS: [],
      SWE: [],
    };

    students.forEach((student) => {
      // split line by commas to isolate types of info
      const row = student.split(',');
      const firstName = row[0].trim();
      const field = row[3].trim();
      if (field === 'CS') {
        students_by_field.CS.push(firstName);
      } else if (field === 'SWE') {
        students_by_field.SWE.push(firstName);
      }
    });

    console.log(`Number of students: ${students.length}`);

    for (const field in students_by_field) {
      const len = students_by_field[field].length;
      console.log(`Number of students in ${field}: ${len}. ` +
        `List: ${students_by_field[field].join(', ')}`
      );
    };
  } catch (error) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
