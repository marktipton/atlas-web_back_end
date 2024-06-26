import { resolve } from 'path';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const promisifiedGet = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  return new Promise((resolve, reject) => {
    client.set(schoolName, value, (err, reply) => {
      resolve(reply);
      console.log(`Reply: ${reply}`);
    });
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await promisifiedGet(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
