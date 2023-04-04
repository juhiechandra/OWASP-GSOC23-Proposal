import json
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['vulnerabilities']
# Create a route for the /vuln_report endpoint
@app.route('/vuln_report', methods=['POST'])
def vuln_report():
    # Get the request data
    data = request.get_json()
    agent_name = data.get('agent_name')
    os_name = data.get('OS')
    timestamp = data.get('timestamp')
    vulnerabilities = data.get('vulnerabilities')

    # Store the data in the MongoDB collection
    doc = {
        'agent_name': agent_name,
        'os_name': os_name,
        'timestamp': timestamp,
        'vulnerabilities': vulnerabilities
    }
    # Insert the document into the collection
    collection.insert_one(doc)
    # Return a success message
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
