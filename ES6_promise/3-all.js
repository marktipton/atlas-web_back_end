import { uploadPhoto, createUser } from 'utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all(promises)
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firtsName} ${user.lastName}`);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}
