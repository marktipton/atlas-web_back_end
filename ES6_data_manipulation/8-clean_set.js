export default function cleanSet(set, startString) {
  const cleanString = Array.from(set)
    .filter(value => value.startsWith(startString))

  return cleanString.join('-');
}
