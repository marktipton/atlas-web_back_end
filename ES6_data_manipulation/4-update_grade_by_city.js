export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  const studentsByLocation = studentsList.filter((students) => students.location === city)
  return studentsByLocation.map((student) => { const gradeObj = newGrades.find(grade => grade.studentId === student.id);
    if (gradeObj) {
      return { ...student, grade: gradeObj.grade };
    } else {
      return student;
    }
  });
}
