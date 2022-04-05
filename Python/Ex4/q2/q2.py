from sys import maxsize
from itertools import permutations
from typing import Callable, Union

INF = float('inf')
INT_MAX = 2147483647
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
GRAPH_8 = [[0, 3, 3], [3, 0, 3], [3, 3, 0]]


def tsp_shortest_path(algorithm: Callable, graph_matrix: Union[list, dict], start: int = DEFAULT_NODE_START):
    """
    # back_tracking:
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_1, start=0)
    80
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_2, start=0)
    -95
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_3, start=0)
    17
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_4, start=0)
    8200
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_5, start=0)
    36
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_6, start=0)
    80
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_7, start=0)
    10
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_8, start=0)
    9

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
    >>> tsp_shortest_path(algorithm=hamilton_cycle, graph_matrix=GRAPH_8, start=0)
    9
    """
    if isinstance(graph_matrix, dict):
        graph_matrix = list(graph_matrix.values())
    return algorithm(graph_matrix, start)


def back_tracking(graph, start):
    """
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_1, start=0)
    80
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_2, start=0)
    -95
    >>> tsp_shortest_path(algorithm=back_tracking, graph_matrix=GRAPH_3, start=0)
    17
    """
    n = len(graph)
    v = [False for _ in range(n)]
    v[start] = True
    answer = []
    back_tracking_rec(graph, v, 0, n, 1, 0, answer)
    return min(answer)


def back_tracking_rec(graph, v, pos, n, count, cost, answer):
    if count == n and graph[pos][0]:
        answer.append(cost + graph[pos][0])
        return
    for i in range(n):
        if v[i] is False and graph[pos][i]:
            v[i] = True
            back_tracking_rec(graph, v, i, n, count + 1,
                              cost + graph[pos][i], answer)
            v[i] = False


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
    print(f"{failures} failures, {tests} tests")
