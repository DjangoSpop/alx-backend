const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = async (number) => {
    const setAsync = promisify(client.set).bind(client);
    await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
    const getAsync = promisify(client.get).bind(client);
    const availableSeats = await getAsync('available_seats');
    return parseInt(availableSeats);
};

app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
    const reservationEnabled = await getCurrentAvailableSeats() > 0;
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
    } else {
        const job = queue.create('reserve_seat').save();
        res.json({ status: 'Reservation in process' });
    }
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });
    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats === 0) {
            reservationEnabled = false;
        } else if (availableSeats >= 0) {
            await reserveSeat(availableSeats - 1);
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });
});

app.listen(1245, () => {
    console.log('Server listening on port 1245');
});
