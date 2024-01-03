export default function appendToEachArrayValue(array, appendString) {
  for (const string of array) {
    array[array.indexOf(string)] = appendString + string;
  }

  return array;
}
