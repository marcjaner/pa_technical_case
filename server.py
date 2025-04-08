from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Added import for CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing any origin

# Google Apps Script URL (deberá ser configurado en el archivo .env)
GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwSSDkQKU58KNlVpPtweEUUpuBCacr_7H1QQ-caa6V29SmM-jbRvrSsrrZfU6WOMgSPTg/exec'

@app.route('/api/process', methods=['GET'])
def process():
    process_id = request.args.get('process_id')
    if not process_id:
        return jsonify({"error": "process_id is required"}), 400
        
    response = requests.get(GOOGLE_SCRIPT_URL, params={"process_id": process_id})
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to get response from Google Apps Script"}), response.status_code
        
    try:
        return jsonify(response.json())
    except ValueError:
        return jsonify({"error": "Invalid response from Google Apps Script"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port)