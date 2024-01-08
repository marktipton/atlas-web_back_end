export default getListStudentIds(studentsList) {
  if (Array.isArray(studentsList)) {
    return studentsList.map(studentsList => studentsList.id);
  } else {
    return [];
  }
}
