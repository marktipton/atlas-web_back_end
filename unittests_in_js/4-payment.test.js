const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let spy;

  this.beforeEach(function() {
    numberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleLogSpy = sinon.spy(console, 'log');
  });

  this.afterEach(function() {
    numberStub.restore();
    consoleLogSpy.restore();
  });

  it('should call utils.calulate number with SUM 200 and 20', function() {
    sendPaymentRequestToApi(200, 20);
    expect(numberStub.calledOnce).to.be.true;
    expect(numberStub.calledWith('SUM', 200, 20)).to.be.true;

    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
  });
});
