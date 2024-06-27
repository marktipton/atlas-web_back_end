import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '9187474249',
  message: 'sup'
};

const job = queue.create('push_notification_code', jobData)
  .save((e) => {
    if (e) {
      console.error('Error creating job:', e);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
