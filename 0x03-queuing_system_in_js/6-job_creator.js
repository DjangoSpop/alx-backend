const kue = require('kue');

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, world!'
};

// Create a queue named push_notification_code
const queueName = 'push_notification_code';

// Create a job with the object created before
const job = queue.create(queueName, jobData);

// When the job is created without error
job.on('enqueue', function() {
    console.log('Notification job created:', job.id);
});

// When the job is completed
job.on('complete', function() {
    console.log('Notification job completed');
});

// When the job is failing
job.on('failed', function() {
    console.log('Notification job failed');
});

// Save the job to the queue
job.save();

// Start processing the queue
queue.process(queueName, function(job, done) {
    // Process the job here
    // ...
    
    // Mark the job as completed
    done();
});
