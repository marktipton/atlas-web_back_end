const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
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

    // console.log(`Number of students: ${students.length}`);
    let output = `Number of students: ${students.length}\n`
    for (const field in students_by_field) {
      const len = students_by_field[field].length;
      output += `Number of students in ${field}: ${len}. ` +
        `List: ${students_by_field[field].join(', ')}\n`;
    };

    console.log(output);
    return output.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
