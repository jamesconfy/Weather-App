from flask import Flask
from config import Config

def create_app():
    app = Flask("weather_app")
    app.config.from_object(Config)

    with app.app_context():
        from weather_app import routes

    return app