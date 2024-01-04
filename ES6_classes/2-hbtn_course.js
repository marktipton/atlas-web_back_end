export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string.');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (typeof students !== 'object') {
      throw new TypeError('Students must be an object');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string.');
    }
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  set students(newStudents) {
    if (typeof newStudents === 'object') {
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an object');
    }
  }
}
