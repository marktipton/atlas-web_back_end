const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  paymentAmount = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${paymentAmount}`);
  return paymentAmount;
}

module.exports = sendPaymentRequestToApi;
