const readDatabase = require('../utils');

const databasePath = process.argv[2];

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const output = await readDatabase(databasePath);
      response.status(200).send(
        `This is the list of our students\n${output}`
      );
    } catch (error) {
      response.status(500).send(`Error: ${error.message}`);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' || major !== 'SWE') {
      response.status(500).send('Major must be CS or SWE');
      return;
    }

    try {
      const output = await readDatabase(databasePath);
      response.status(200).send(`List of students in ${major}:\n${output}`);
    } catch (error) {
      response.status(500).send(`Error: ${error.message}`);
    }
  }
}

module.exports = StudentsController;
