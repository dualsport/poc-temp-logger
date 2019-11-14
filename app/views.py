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
        return (
            f"""
            <div>
                Cambria Temperature Monitoring: 
                <a href="/index">Home</a> 
                <a href="/logtemps">Log Temps</a>
            </div>
                <h1>You Entered</h1>
            <p>Name: {form.username.data}</p>
            <p>Machine: {form.machine.data}</p>
            <p>Main Temp: {form.maintemp.data}</p>
            <p>Aux Temp: {form.auxtemp.data}</p>
            <button onclick="window.location.href = '/logtemps';">Continue</button>
            """
        )
    return render_template('temps.html', title='Temp Logs', form=form)
