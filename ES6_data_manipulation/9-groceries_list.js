export default function groceriesList() {
  const groceryList = {
    Apples: 10,
    Tomatoes: 10,
    Pasta: 1,
    Rice: 1,
    Banana: 5,
  };
  const groceryMap = new Map(Object.entries(groceryList));
  return groceryMap;
}
