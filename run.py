"""
This is the application's entry point. We'll run this file to start the Flask server and launch our application.

To use the command flask run like we did before, we would need to set the FLASK_APP environment variable to run.py, like so:

- set FLASK_APP=run.py
- flask run
"""

from app import app

if __name__ == '__main__':
    app.run()
