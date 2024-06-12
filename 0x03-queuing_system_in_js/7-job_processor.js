const kue = require('kue');

const blacklistedNumbers = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklistedNumbers.includes(phoneNumber)) {
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
        return done(error);
    }

    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // Create a queue with Kue and process the job here
    
}
const queue = kue.createQueue();

// Process the jobs
queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

// Create the queue with Kue and process the jobs
// Make sure to set up the Redis server and run two node processes

module.exports = sendNotification;
