from app import app
from flask import render_template
from app.forms import TempForm


@app.route('/')
@app.route('/index')
def index():
    return (
        """
        <div>
            Cambria Temperature Monitoring:
            <a href="/logtemps">Log Temps</a>
        </div>
        <h1>Hello, Cambria!</h1>
        """
    )


# Add
@app.route('/logtemps', methods=['GET', 'POST'])
def logtemps():
    form = TempForm()
    if form.validate_on_submit():
        # Do stuff
        return render_template('ack.html', title='Temp Logs', form=form)
    return render_template('temps.html', title='Temp Logs', form=form)
