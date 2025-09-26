from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Serve frontend files
@app.route('/')
def serve_frontend():
    # Get the path to the frontend directory (go up two levels from api/ to backend/ then to frontend/)
    frontend_path = os.path.join(os.path.dirname(__file__), '../../frontend')
    return send_from_directory(frontend_path, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    frontend_path = os.path.join(os.path.dirname(__file__), '../../frontend')
    return send_from_directory(frontend_path, path)

# Test route
@app.route('/test')
def test():
    return {'status': 'ok', 'message': 'Flask is working!'}

from . import routes
from . import utils

print("=== Flask App Initialized ===")