import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api import app

if __name__ == "__main__":
    app.run()

application = app  # gunicorn looks for 'application' by default