const readDatabase = require('../utils');

const databasePath = process.argv[2];

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const output = await readDatabase(databasePath);
      response.status(200).send(
        `This is the list of our students\n${output}`,
      );
    } catch (error) {
      response.status(500).send(`Error: ${error.message}`);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major must be CS or SWE');
    }

    try {
      const data = await readDatabase(databasePath);
      const lines = data.split('\n');
      const majorLine = lines.find((line) => line.includes(
        `Number of students in ${major}`,
      ));
      let studentNames = '';
      if (majorLine) {
        studentNames = majorLine.split('List: ')[1];
      }
      response.status(200).send(`List: ${studentNames}`);
    } catch (error) {
      console.error('Error reading database:', error);
      response.status(500).send(`Error: ${error.message}`);
    }
  }
}

module.exports = StudentsController;
