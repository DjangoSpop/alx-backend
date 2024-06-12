const redis = require('redis');

// Create Redis client
const client = redis.createClient();

// On connect
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// On error
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// On message
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
