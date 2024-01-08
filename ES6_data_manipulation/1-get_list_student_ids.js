export default function getListStudentIds(studentsList) {
  if (Array.isArray(studentsList)) {
    return studentsList.map(studentsList => studentsList.id);
  } else {
    return [];
  }
}
