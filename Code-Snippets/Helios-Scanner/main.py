from flask import Flask, jsonify, request
from helios import Helios

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    # Get the request data
    data = request.get_json()
    url = data.get('url')
    scan_type = data.get('scan_type')
    
    # Create Helios object and perform scan
    helios = Helios()
    results = helios.scan(url, scan_type)
    
    # Return results as JSON
    return jsonify(results)

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
