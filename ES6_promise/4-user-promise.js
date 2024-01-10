export default function signUpUser(firstName, lastName) {
  const promise = new Promise((resolve, reject) => {
    const a = true;
    if (a) {
      const promiseObject = {
        firstName: firstName,
        lastName: lastName,
      };
      resolve(promiseObject);
    } else {
      reject(new Error('Reject'));
    }
  });
  return promise;
}
