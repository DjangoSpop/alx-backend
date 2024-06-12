function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((job) => {
        const jobID = queue.create('push_notification_code_3', job).save((err) => {
            if (err) {
                console.log(`Notification job ${jobID} failed: ${err}`);
            } else {
                console.log(`Notification job created: ${jobID}`);
            }
        });

        jobID.on('complete', () => {
            console.log(`Notification job ${jobID} completed`);
        });

        jobID.on('progress', (progress) => {
            console.log(`Notification job ${jobID} ${progress}% complete`);
        });
    });
}
