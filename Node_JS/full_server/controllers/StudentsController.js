const readDatabase = require('./utils');

class StudentsController {
  static getAllStudents(request, response) {
    response.status(200).send(
      `This is the list of our students\n${readDatabase}`
    );
  }

  static getAllStudentsByMajor(request, response, major) {
    if (major !== 'CS' || major !== 'SWE') {
      console.error('Major entered does not exist')
    }
  }
}

module.exports = StudentsController;
