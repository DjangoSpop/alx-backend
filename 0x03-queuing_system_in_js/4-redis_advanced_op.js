const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Store a hash value using hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display the object stored in Redis using hgetall
client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
        console.error(err);
    } else {
        console.log(result);
    }
});

// Close the Redis client
client.quit();
