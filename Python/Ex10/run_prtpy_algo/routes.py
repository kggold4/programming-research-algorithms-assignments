from flask import render_template, redirect, url_for

from run_prtpy_algo import app
from run_prtpy_algo.forms import InputForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input_form():
    form = InputForm()
    is_submitted = form.validate_on_submit()
    if not is_submitted:
        return render_template('input.html', form=form)
    else:
        return redirect(url_for(show_results.__name__))


@app.route('/results', methods=['GET', 'POST'])
def show_results():
    return render_template('results.html')
