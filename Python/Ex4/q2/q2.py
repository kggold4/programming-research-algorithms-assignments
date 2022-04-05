from sys import maxsize
from itertools import permutations
from typing import Callable, Union
import numpy as np
import math

INF = float('inf')
EPSILON = 0.001
DEFAULT_NODE_START = 0
GRAPH_1 = {'x': [0, 10, 15, 20], 'y': [10, 0, 35, 25], 'z': [15, 35, 0, 30], 'w': [20, 25, 30, 0]}
GRAPH_2 = [[0, -10, -15, -20], [-10, 0, -35, -25], [-15, -35, 0, -30], [-20, -25, -30, 0]]
GRAPH_3 = [[0, 2, 3, 4], [2, 0, 6, 5], [3, 6, 0, 7], [4, 5, 7, 0]]
GRAPH_4 = [[0, 200, 4000], [200, 0, 4000], [4000, 4000, 0]]
GRAPH_5 = {'v1': [0, 18], 'v2': [18, 0]}
GRAPH_6 = [[0, 5, 10, 15, 20, 25], [5, 0, 10, 15, 20, 25], [5, 10, 0, 15, 20, 25],
           [5, 10, 15, 0, 20, 25], [5, 10, 15, 20, 0, 25], [5, 10, 15, 20, 25, 0]]
GRAPH_7 = {'a': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'b': [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
           'c': [8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 'd': [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],
           'e': [6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 'f': [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],
           'g': [4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 'h': [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
           'i': [2, 3, 4, 5, 6, 7, 8, 9, 0, 1], 'j': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]}


def tsp_shortest_path(algorithm: Callable, graph_matrix: Union[list, dict], start: int = DEFAULT_NODE_START):
    """
    # greedy:
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_1, start=0)
    140.23408737444413
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_2, start=0)
    140.23408737444413
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_3, start=0)
    28.216277698516947
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_4, start=0)
    13912.222742395275
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_5, start=0)
    50.91168824543142
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_6, start=0)
    133.45214505324043
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_7, start=0)
    94.8683298050514

    # hamilton_cycle:
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_1, start=0)
    80
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_2, start=0)
    -95
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_3, start=0)
    17
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_4, start=0)
    8200
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_5, start=0)
    36
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_6, start=0)
    80
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_7, start=0)
    10
    """
    if isinstance(graph_matrix, dict):
        graph_matrix = list(graph_matrix.values())
    return algorithm(graph_matrix, start)


def greedy(graph_matrix: list, start: int):
    """
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_1, start=0)
    140.23408737444413
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_2, start=0)
    140.23408737444413
    >>> tsp_shortest_path(algorithm=greedy, graph_matrix=GRAPH_5, start=0)
    50.91168824543142
    """
    graph_matrix = np.array(graph_matrix)
    n = graph_matrix.shape[0]
    dist = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            dist[i, j] = math.sqrt(np.sum((graph_matrix[i, :] - graph_matrix[j, :]) ** 2))

    step = sum_path = 0
    path = [start]
    for i in range(1, n):
        temp_distance = INF
        for j in range(1, n):
            flag = False
            if j in path:
                flag = True
            if flag is False and dist[j][path[i - 1]] < temp_distance:
                step = j
                temp_distance = dist[j][path[i - 1]]
        path.append(step)
        sum_path += temp_distance
    sum_path += dist[0][step]
    return sum_path


def hamilton_cycle(graph_matrix: list, start: int):
    """
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_1, start=0)
    80
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_2, start=0)
    -95
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_7, start=0)
    10
    """
    vertex = []
    for i in range(len(graph_matrix)):
        if i != start:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path_weight = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # current path weight
        path_weight = 0

        # calculate current path weight
        k = start
        for j in i:
            path_weight += graph_matrix[k][j]
            k = j
        path_weight += graph_matrix[k][start]

        # update min_path_weight
        min_path_weight = min(min_path_weight, path_weight)

    return min_path_weight


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
