export default function getStudentIdsSum(studentsList) {
  // add id to the accumulator w/ initial value set to zero below
  const idSum = studentsList.reduce((accumulator, student) => {
    return accumulator + student.id;
  }, 0);
  return Number(idSum);
}
