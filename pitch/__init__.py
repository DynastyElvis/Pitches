
from flask import Flask #, render_template
from flask_sqlalchemy import SQLAlchemy #, SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__) #, template_folder='templates')
app.config['SECRET_KEY'] = '564648sjdhbfl654684adfa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'minutepitcher'
app.config['MAIL_PASSWORD'] = '5594'
mail = Mail(app)

from pitch import routes