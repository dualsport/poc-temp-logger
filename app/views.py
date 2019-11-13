from app import app
# Add
from flask import render_template
from app.forms import TempForm


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


# Add
@app.route('/logtemps', methods=['GET', 'POST'])
def logtemps():
    form = TempForm
    return render_template('temps.html', title='Temp Logs', form=form)
