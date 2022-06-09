from prtpy.partitioning.ckk import ckk
from prtpy.partitioning.irnp import irnp
from prtpy.partitioning.kk import kk
from prtpy.partitioning.rnp import rnp
from run_prtpy_algo.objects.algorithm_response import AlgorithmResponse

algorithm_functions = {"kk": kk, "ckk": ckk, "rnp": rnp, "irnp": irnp}


def get_input_items(items: str) -> list:
    return [int(number) for number in items.split(',')]


def get_algorithm_by_name(name: str):
    return algorithm_functions[name]


def get_algorithm_response(algo_request):
    algorithm_name = algo_request.get('algorithm')
    algorithm = get_algorithm_by_name(algorithm_name)
    items = algo_request.get('items')
    num_of_bins = int(algo_request.get('num_of_bins'))

    error = ''
    if algorithm_name == 'kk' and num_of_bins > 2:
        error = f"Input Error: KK algorithm is capable with two bins only,\ngot {num_of_bins}!"
        result_bins = []  # empty bins
        sums = []
    else:
        from prtpy import partition
        result_bins = partition(algorithm=algorithm, numbins=num_of_bins, items=items)
        sums = [sum(s) for s in result_bins]
    return AlgorithmResponse(name=algorithm_name, bins=result_bins, sums=sums, error=error)
