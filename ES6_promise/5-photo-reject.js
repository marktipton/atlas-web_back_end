export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    if (fileName.endsWith('.jpg')) {
      resolve(`File ${fileName} uploaded successfully.`);
    } else {
      reject(new Error(`Error: ${fileName} cannot be processed.`));
    }
  });
}
