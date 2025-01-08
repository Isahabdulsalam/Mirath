from flask import Flask
from flask_mysqldb import MySQL
from config import Config

# Initialize the app
app = Flask(__name__)

# Load configuration from the Config class in config.py
app.config.from_object(Config)

# Initialize MySQL connection
mysql = MySQL(app)

def create_app():
    # Import routes and register with the app
    from app import routes
    return app
