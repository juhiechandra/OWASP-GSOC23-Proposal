from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
import time

# Create a Flask app
app = Flask(__name__)

# Define the job to be executed by the scheduler
def job():
    # Code to be executed by the job
    print("Hello, world!")

# Create a background scheduler and start it
scheduler = BackgroundScheduler()
scheduler.start()

# Define a route to schedule a job via POST request
@app.route('/schedule-job', methods=['POST'])
def schedule_job():
    # Get the start time, interval, and day of week from the request JSON
    start_time = request.json.get('start_time')
    interval = request.json.get('interval')
    day_of_week = request.json.get('day_of_week')

    # Add the job to the scheduler with the specified parameters
    scheduler.add_job(job, 'interval', minutes=interval, start_date=start_time, day_of_week=day_of_week)
    
    # Return a success response
    return jsonify({'status': 'success'})

# Run the Flask app
if __name__ == '__main__':
    app.run()
