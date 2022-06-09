import json

from flask import render_template, redirect, url_for, request
from run_prtpy_algo import app
from run_prtpy_algo.forms import InputForm
from run_prtpy_algo.objects.algorithm_request import AlgorithmRequest
from run_prtpy_algo.utils import get_input_items, get_algorithm_response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input_form():
    form = InputForm()
    is_submitted = form.validate_on_submit()

    # input form not completed
    if not is_submitted:
        return render_template('input.html', form=form)

    # get algorithm request and sent it by json format
    else:
        algo_request = AlgorithmRequest(items=get_input_items(form.items.data),
                                        num_of_bins=int(form.num_of_bins.data),
                                        algorithm=form.algorithm.data)
        return redirect(url_for(show_results.__name__, algo_request=algo_request.to_json()))


@app.route('/results', methods=['GET', 'POST'])
def show_results():
    # convert the algorithm request from json to object and get response
    algo_request = request.args['algo_request']
    algo_response = get_algorithm_response(json.loads(algo_request))
    return render_template('results.html', algo_response=algo_response)
