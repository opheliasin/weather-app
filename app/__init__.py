from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# app.register_blueprint(routes, url_prefix = "/")
