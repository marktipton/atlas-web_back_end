export default function getStudentIdsSum(studentsList) {
  const idSum = studentsList.reduce((accumulator, student) => {
    // add id to the accumulator w/ initial value set to zero below
    return accumulator + student.id;
  }, 0);
  return Number(idSum);
}
