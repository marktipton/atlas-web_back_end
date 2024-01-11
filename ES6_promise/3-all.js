import {uploadPhoto, createUser} from './5-photo-reject';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all(promises)
    .then(([photo, user]) => {
      console.log(`Body: ${user.firtsName} ${user.lastName}`);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}
