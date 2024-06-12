const redis = require('redis');

const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
function publishMessage(message , time){
    const publisher = redis.createClient();
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school channel', message);
    }, time);
    setTimeout(() => {
        publisher.quit();
    }, 7000); 
}
