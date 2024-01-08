export default function updateUniqueItems(foodMap) {
  if (!(foodMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  const updatedMap = new Map();

  foodMap.forEach((quantity, item) => {
    if (quantity === 1) {
      // replace with 100
      updatedMap.set(item, 100);
    } else {
      // use original value
      updatedMap.set(item, quantity);
    }
  });
}
