const redis = require('redis');
const promisify = require('proisify');
const connectRedis = async () => {
  const client = redis.createClient()
    .on('error', err => console.log('Redis Client Error', err))
    .connect();

  await client.set('key', 'value');
  const value = await client.get('key');

  if (client.isReady()) {
    console.log('Redis client connected to the server');
    await client.disconnect();
  } else {
    console.log('Redis client not connected to the server: ERROR_MESSAGE');
  }

  function setNewSchool(SchoolName, Value) {
    client.set(SchoolName);
    client.set(SchoolName, Value, (err, reply) => {
      if (err) {
        console.log('Error setting value:', err);
      } else {
        console.log('Value set:', reply);
      }
    });
  }

  async function displaySchoolValue(SchoolName) {
    await client.get(SchoolName, (err, reply) => {
      if (err) {
        console.log('Error getting value:', err);
      } else {
        console.log('Value of', SchoolName, 'is:', reply);
      }
    });
  }
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisico', '100');
  displaySchoolValue('HolbertonSanFransisco');
  module.exports = { setNewSchool, displaySchoolValue };


};


