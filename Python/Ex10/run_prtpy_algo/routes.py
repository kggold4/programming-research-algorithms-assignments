import json

from flask import render_template, redirect, url_for, request, session

from prtpy.partitioning.ckk import ckk
from prtpy.partitioning.irnp import irnp
from prtpy.partitioning.kk import kk
from prtpy.partitioning.rnp import rnp
from run_prtpy_algo import app
from run_prtpy_algo.forms import InputForm
from run_prtpy_algo.static.my_objects.algorithm_request import AlgorithmRequest
from run_prtpy_algo.static.my_objects.algorithm_response import AlgorithmResponse


@app.route('/')
def index():
    return render_template('index.html')


def _get_input_items(items: str) -> list:
    return [int(number) for number in items.split(',')]


def _get_algorithm_by_name(name: str):
    if name == "kk":
        return kk
    elif name == "ckk":
        return ckk
    elif name == "rnp":
        return rnp
    elif name == "irnp":
        return irnp
    else:
        raise ValueError(f"Unknown algorithm named: {name}")


def _get_algorithm_response(algo_request):
    algorithm = _get_algorithm_by_name(algo_request.get('algorithm'))
    items = algo_request.get('items')
    num_of_bins = int(algo_request.get('num_of_bins'))
    from prtpy import partition
    result_bins = partition(algorithm=algorithm, numbins=num_of_bins, items=items)
    return AlgorithmResponse(bins=result_bins, sums=[sum(s) for s in result_bins])


@app.route('/input', methods=['GET', 'POST'])
def input_form():
    form = InputForm()
    is_submitted = form.validate_on_submit()
    if not is_submitted:
        return render_template('input.html', form=form)
    else:
        algo_request = AlgorithmRequest(items=_get_input_items(form.items.data),
                                        num_of_bins=int(form.num_of_bins.data),
                                        algorithm=form.algorithm.data)
        return redirect(url_for(show_results.__name__, algo_request=algo_request.to_json()))


@app.route('/results', methods=['GET', 'POST'])
def show_results():
    algo_request = request.args['algo_request']
    algo_response = _get_algorithm_response(json.loads(algo_request))
    print(algo_response)
    return render_template('results.html', algo_response=algo_response)
