const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
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

    // console.log(`Number of students: ${students.length}`);
    let output = `Number of students: ${students.length}\n`;
    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const len = studentsByField[field].length;
        output += `Number of students in ${field}: ${len}. `
          + `List: ${studentsByField[field].join(', ')}\n`;
      }
    }

    console.log(output);
    return output.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
