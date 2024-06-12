const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('../createPushNotificationsJobs');

describe('createPushNotificationsJobs', () => {
    let queue;

    before(() => {
        // Create a new queue instance
        queue = kue.createQueue();
        // Enter test mode without processing the jobs
        queue.testMode.enter();
    });

    after(() => {
        // Clear the queue and exit test mode
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should add jobs to the queue', () => {
        // Call the createPushNotificationsJobs function
        createPushNotificationsJobs(queue, 10, 'Welcome to GitHub Copilot');

        // Get the list of jobs in the queue
        const jobs = queue.testMode.jobs;

        // Assert that the correct number of jobs were added
        expect(jobs.length).to.equal(10);

        // Assert that each job has the correct properties
        jobs.forEach((job) => {
            expect(job.type).to.equal('push_notification_code');
            expect(job.data).to.deep.equal({ message: 'Welcome to GitHub Copilot' });
        });
    });

    // Add more test cases as needed

});
