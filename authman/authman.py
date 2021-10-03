from flask import Flask, Blueprint
from flask_restful import Api

from authman.config import Config

apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

from authman import resource
def create_app():
	app = flask(__name__)
	app.config.from_object(Config) # Loads Application Config
	app.register_blueprint(apiv1_bp) # Loads API V1
	return app
