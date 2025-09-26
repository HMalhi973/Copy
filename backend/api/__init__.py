from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Test route - add this
@app.route('/test')
def test():
    return {'status': 'ok', 'message': 'Flask is working!'}

from . import routes
from . import utils

print("=== Flask App Initialized ===")

