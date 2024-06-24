const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let spy;

  this.beforeEach(function() {
    spy = sinon.spy(Utils, 'calculateNumber');
  });

  this.afterEach(function() {
    spy.restore();
  });

  it('should call utils.calulate number with SUM 200 and 20', function() {
    sendPaymentRequestToApi(200, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 200, 20)).to.be.true;
  });
});
