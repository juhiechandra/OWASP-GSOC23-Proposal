import axios from 'axios';

// This function will be called from the frontend to schedule a job
const scheduleJob = async (start_time, interval, day_of_week) => {
  try {
    // Send a POST request to the backend
    // The backend will schedule the job and return the job id
    const response = await axios.post('/schedule-job', {
      start_time: start_time,
      interval: interval,
      day_of_week: day_of_week
    });
    // Do something with the response
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

scheduleJob('2023-04-01 12:00:00', 12, 'tue'); // Example usage
