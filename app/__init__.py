from flask import Flask
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flaskext.markdown import Markdown



app = Flask(__name__)
bootstrap = Bootstrap(app)
fa = FontAwesome(app)
Markdown(app)

from app import routes