from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cambria-is-number-one'

from app import views
