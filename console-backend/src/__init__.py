import os

from flask import Flask
from flask_cors import CORS

from .initial_dataset import load_initial_dataset

load_initial_dataset()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # allow CORS for all domains on all routes
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings) 

    # register blueprints
    from src.api.query import query_blueprint
    app.register_blueprint(query_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app
