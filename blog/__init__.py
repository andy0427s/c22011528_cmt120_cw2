from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor


app = Flask(__name__)
app.config['SECRET_KEY'] = '<52f2f7bbd0899acac4c4cc57bad53e4bc96af3abc9128ff2>'

# DB Connection

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22011528:Twente0508$@csmysql.cs.cf.ac.uk:3306' \
                                        '/c22011528_mydb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# CKeditor
ckeditor = CKEditor(app)

from blog import routes

