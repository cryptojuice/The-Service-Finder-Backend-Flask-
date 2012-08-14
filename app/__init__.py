from flask import Flask
from app import settings
from views.views import main
from werkzeug.contrib.fixers import ProxyFix

app = Flask("app")
app.register_blueprint(main)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app)
