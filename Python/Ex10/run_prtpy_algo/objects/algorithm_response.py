import json

from prtpy.utils import calculate_diff

algorithm_descriptions = {"kk": "Karmarkar-karp", "ckk": "Complete Karmarkar-Karp",
                          "rnp": "Recursive Number Partitioning", "irnp": "Improved Recursive Number Partitioning"}


class AlgorithmResponse:
    def __init__(self, name: str, bins: list[list[int]], sums: list[int], error: str = ''):
        self.name = name
        self.description = algorithm_descriptions[name]
        self.bins = bins
        self.sums = sums
        self.length = len(self.bins)
        self.diff_sum = calculate_diff(bins)
        self.error = error

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def get_algorithms_choices():
    result = []
    for key, value in algorithm_descriptions.items():
        result.append((key, value))
    return result
