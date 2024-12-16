from flask import Flask

from src.main.routes.bank_account_routes import bank_routes_bp
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(bank_routes_bp)
