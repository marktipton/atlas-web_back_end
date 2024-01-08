export default function getStudentsByLocation(studentsList, city) {
  const studentsByLocation = studentsList.filter(students => students.location === city);
  return studentsByLocation;
}
