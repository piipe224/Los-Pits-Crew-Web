from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://dfba:Dfb128@localhost:5432/lpc_db"

db.init_app(app)
