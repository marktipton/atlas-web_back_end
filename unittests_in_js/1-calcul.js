function calculateNumber(type, a, b) {
  roundA = Math.round(a);
  roundB = Math.round(b);
  if (type === 'SUM') {
    return roundA + roundB;
  } else if (type === 'SUBTRACT') {
    return roundA - roundB;
  } else if (type === 'DIVIDE') {
    if (roundB === 0) {
      return 'Error';
    }
    return (roundA / roundB);
  }
}

module.exports = calculateNumber;
