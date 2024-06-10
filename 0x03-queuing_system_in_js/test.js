const redis = require('redis');
const client = redis.createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.set('Holberton', 'School', redis.print);
client.get('Holberton', (err, reply) => {
  console.log(reply);
});
