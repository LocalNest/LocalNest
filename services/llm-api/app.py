import os
import json
import subprocess
import sys
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Get Ollama base URL from environment
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint - runs the chat.py script with the provided payload"""
    try:
        # Validate request
        if request.content_type != 'application/json':
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        payload = request.json
        if not payload:
            return jsonify({"error": "No JSON payload provided"}), 400
        
        # Run the chat script
        env = os.environ.copy()
        env['OLLAMA_BASE_URL'] = OLLAMA_BASE_URL
        
        result = subprocess.run(
            ['python3', '-u', 'scripts/chat.py'],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            env=env,
            timeout=60
        )
        
        if result.returncode != 0:
            logging.error(f"Chat script error: {result.stderr}")
            return jsonify({"error": "Chat script failed", "details": result.stderr}), 500
        
        # Parse and return the response
        try:
            response_data = json.loads(result.stdout)
            return jsonify(response_data), 200
        except json.JSONDecodeError:
            # If not JSON, return as text
            return jsonify({"response": result.stdout}), 200
            
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Request timeout"}), 504
    except Exception as e:
        logging.error(f"Chat endpoint error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/code', methods=['POST'])
def code():
    """Code endpoint - runs the code.py script with the provided payload"""
    try:
        # Validate request
        if request.content_type != 'application/json':
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        payload = request.json
        if not payload:
            return jsonify({"error": "No JSON payload provided"}), 400
        
        # Default language if not specified
        if 'language' not in payload:
            payload['language'] = 'python'
        
        # Run the code script
        env = os.environ.copy()
        env['OLLAMA_BASE_URL'] = OLLAMA_BASE_URL
        
        result = subprocess.run(
            ['python3', '-u', 'scripts/code.py'],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            env=env,
            timeout=60
        )
        
        if result.returncode != 0:
            logging.error(f"Code script error: {result.stderr}")
            return jsonify({"error": "Code script failed", "details": result.stderr}), 500
        
        # Parse and return the response
        try:
            response_data = json.loads(result.stdout)
            return jsonify(response_data), 200
        except json.JSONDecodeError:
            # If not JSON, return as text
            return jsonify({"response": result.stdout}), 200
            
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Request timeout"}), 504
    except Exception as e:
        logging.error(f"Code endpoint error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)