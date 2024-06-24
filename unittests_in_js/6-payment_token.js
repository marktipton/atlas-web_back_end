function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API'});
  } else {
    // return empty promise on false this promise will resolve immediately
    return new Promise(() => {});
  }
}

module.exports = getPaymentTokenFromAPI;
