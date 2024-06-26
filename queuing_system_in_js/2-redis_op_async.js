import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const promisifiedGet = promisify(client.get).bind(client);
const promisifiedSet = promisify(client.set).bind(client);


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

async function setNewSchool(schoolName, value) {
  try {
    const reply = await promisifiedSet(schoolName, value);
    console.log(`Reply: ${reply}`);
  } catch (err) {
    console.error(err);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await promisifiedGet(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
