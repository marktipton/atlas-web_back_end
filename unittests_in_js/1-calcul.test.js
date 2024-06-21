// 0-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('should return 4 when inputs are 1 and 3', function() {
    assert.strictEqual(calculateNumber(1, 3, 'SUM'), 4);
  });

  it('should return 5 when inputs are 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7, 'SUM'), 5);
  });

  it('should return 6 when inputs are 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7, 'SUM'), 6);
  });

  it('should return 0 when inputs are 0.3 and -0.43', function() {
    assert.strictEqual(calculateNumber(0.3, -0.43, 'SUM'), 0);
  });

  it('should return -3 when inputs are -0.7 and -1.7', function() {
    assert.strictEqual(calculateNumber(-0.7, -1.7, 'SUM'), -3);
  });

  it('should return 0 when inputs are 0 and 0', function() {
    assert.strictEqual(calculateNumber(0, 0, 'SUM'), 0);
  });
  // unittests for SUBTRACT
  it('should return -2 when inputs are 1 and 3', function() {
    assert.strictEqual(calculateNumber(1, 3, 'SUBTRACT'), -2);
  });

  it('should return -3 when inputs are 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7, 'SUBTRACT'), -3);
  });

  it('should return -2 when inputs are 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7, 'SUBTRACT'), -2);
  });

  it('should return 0 when inputs are 0.3 and -0.43', function() {
    assert.strictEqual(calculateNumber(0.3, -0.43, 'SUBTRACT'), 0);
  });

  it('should return 1 when inputs are -0.7 and -1.7', function() {
    assert.strictEqual(calculateNumber(-0.7, -1.7, 'SUBTRACT'), 1);
  });

  it('should return 0 when inputs are 0 and 0', function() {
    assert.strictEqual(calculateNumber(0, 0, 'SUBTRACT'), 0);
  });
  // DIVIDE tests:
  it('should return 2 when inputs are 6 and 3', function() {
    assert.strictEqual(calculateNumber(6, 3, 'DIVIDE'), 2);
  });

  it('should return 0.5 when inputs are 1.2 and 2', function() {
    assert.strictEqual(calculateNumber(1.2, 2, 'DIVIDE'), 0.5);
  });

  it('should return 1 when inputs are 1.5 and 2', function() {
    assert.strictEqual(calculateNumber(1.5, 2, 'DIVIDE'), 1);
  });

  it('should return Error when inputs are 0.3 and -0.43', function() {
    assert.strictEqual(calculateNumber(0.3, -0.43, 'DIVIDE'), 'Error');
  });

  it('should return 0.5 when inputs are -0.7 and -1.7', function() {
    assert.strictEqual(calculateNumber(-0.7, -1.7, 'DIVIDE'), 0.5);
  });

  it('should return Error when inputs are 0 and 0', function() {
    assert.strictEqual(calculateNumber(0, 0, 'DIVIDE'), 'Error');
  });
});