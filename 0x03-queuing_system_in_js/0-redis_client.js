import { createClient } from 'redis';

const client = await createClient() 
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
