export default class Building {
  constructor(sqft) {
    // if (new.target === Building) {
    //   throw new TypeError('Abstract class Building cannot be instantiated directly');
    // }
    this._sqft = sqft;
    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new TypeError('Class extending Building must override evacuationWarningMessage.');
    }
  }

  get sqft() {
    return this._sqft;
  }
}
