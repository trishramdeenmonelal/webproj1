from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:lab5@localhost/webproj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views