from flask import Flask, render_template, jsonify, request
from pynput.keyboard import Key, Controller
import threading
import time
import os
import sys
import subprocess

app = Flask(__name__, template_folder='frontend')
#CORS(app)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to serve data to the frontend
@app.route('/api/data')
def get_data():
    # You can return any data here (e.g., from a database)
    data = {"message": "Hello from the Python backend!"}
    return jsonify(data)

@app.route('/first_finch_test', methods=['POST'])
def first_finch_test():
    script_path = os.path.join('backend', 'meow.py')
    try:
        result = subprocess.check_output(
            [sys.executable, script_path],
            text=True,
            stderr=subprocess.STDOUT
        )
        return jsonify({"status": "success", "output": result.strip()})

    except FileNotFoundError:
        error_msg = f"Error: The file '{script_path}' was not found."
        print(error_msg)
        return jsonify({"status": "error", "message": error_msg}), 500

    except Exception as e:
        print(f"General Error: {str(e)}")
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

