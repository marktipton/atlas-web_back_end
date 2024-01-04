import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const class1 = ClassRoom(19);
  const class2 = ClassRoom(20);
  const class3 = ClassRoom(34);
  const classArray = [class1, class2, class3];
  return classArray;
}
