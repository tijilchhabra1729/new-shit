import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail, Message
from dotenv import load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import os
from oauthlib.oauth2 import WebApplicationClient
import requests

load_dotenv()
app =  Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.update({
    'OAUTH1_PROVIDER_ENFORCE_SSL': False
})
app.config['SECRET_KEY'] = 'secret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'sneaker_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

GOOGLE_CLIENT_ID = '473490364377-mr543r3jrc951kh23c7fad4prn1n7pm8.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

db = SQLAlchemy(app)
Migrate(app,db)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def create_db(app):
    with app.app_context():
        db.create_all()
        
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
