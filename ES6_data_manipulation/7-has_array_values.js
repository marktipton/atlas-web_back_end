export default function hasValuesFromArray(set, array) {
  const checkSet = array.every(element => set.has(element));
  return checkSet;
}
