export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const cleanString = Array.from(set)
    .filter(value => value.startsWith(startString))
    .map(value => value.substring(startString.length));
  return cleanString.join('-');
}
