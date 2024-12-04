from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://heulwen:%s@localhost/saleapp?charset=utf8mb4" % quote('Nguyennguyen123@')
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 5
app.config["SECRET_KEY"] = "git.heulwen.tech"

db = SQLAlchemy(app)
login = LoginManager(app)

cloudinary.config(
    cloud_name = "dwivkhh8t",
    api_key = "925656835271691",
    api_secret = "xggQhqIzVzwLbOJx05apmM4Od7U",
    secure=True
)