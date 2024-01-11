export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    const a = true;
    if (!a) {
      resolve(`File ${fileName} uploaded successfully.`);
    } else {
      reject(new Error(`${fileName} cannot be processed.`));
    }
  });
}
