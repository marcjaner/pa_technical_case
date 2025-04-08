from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Added import for CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing any origin

# Google Apps Script URL (deberá ser configurado en el archivo .env)
GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyrWpzV0NeNqTtOEH0oZ0Ne3Xgek24M6errG1WeYUOOiCYKQNjWF2kcw3L9kOdYnPbL/exec'

@app.route('/api/process', methods=['GET'])
def process():
    process_id = request.args.get('process_id')
    payload = {
        "process_id": process_id,
    }
    response = requests.post(GOOGLE_SCRIPT_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)