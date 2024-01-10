export default function getFullResponseFromAPI(success) {
  const promise = new Promise((resolve, reject) => {
    if (success) {
      const apiResponse = {
        status: 200,
        body: 'Success'
      };
      resolse(apiResponse);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });

  return promise;
}
