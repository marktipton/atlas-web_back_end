export default function appendToEachArrayValue(array, appendString) {
  let appendArray = {}
  for (const string of array) {
    appendArray[array.indexOf(string)] = appendString + string;
  }

  return appendArray;
}
