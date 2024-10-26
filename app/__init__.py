from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Initialize the database with the Flask app
    db.init_app(app)

    # Register the blueprint from routes.py
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Log working directory and template path
   # print(f"Current working directory: {os.getcwd()}")
    #print(f"Index.html exists: {os.path.exists('app/templates/index.html')}")
    # Return the initialized Flask app
    return app
