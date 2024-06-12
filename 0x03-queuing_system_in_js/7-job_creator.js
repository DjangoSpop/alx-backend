const kue = require('kue');

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const queue = kue.createQueue();

jobs.forEach((job, index) => {
    const notificationJob = queue.create('push_notification_code_2', job)
        .save((err) => {
            if (!err) {
                console.log(`Notification job created: ${notificationJob.id}`);
            }
        });

    notificationJob.on('complete', () => {
        console.log(`Notification job ${notificationJob.id} completed`);
    });

    notificationJob.on('failed', (err) => {
        console.log(`Notification job ${notificationJob.id} failed: ${err}`);
    });

    notificationJob.on('progress', (progress) => {
        console.log(`Notification job ${notificationJob.id} ${progress}% complete`);
    });
});

queue.process('push_notification_code_2', (job, done) => {
    // Process the job here
    // ...
    done();
});

queue.on('error', (err) => {
    console.log(`Queue error: ${err}`);
});

queue.on('job enqueue', () => {
    console.log('Job enqueued');
});

queue.on('job complete', (id) => {
    kue.Job.get(id, (err, job) => {
        if (err) return;
        job.remove((err) => {
            if (err) throw err;
            console.log(`Job ${job.id} removed from queue`);
        });
    });
});

queue.on('job failed', (id, err) => {
    console.log(`Job ${id} failed: ${err}`);
});

queue.on('job progress', (id, progress) => {
    console.log(`Job ${id} ${progress}% complete`);
});
