"""
Programming Research Algorithms Course 2022, Ariel University
Assignment #5

@Author: Kfir Goldfarb
@Date: 26/04/2022

Implementing the main algorithms in the:
    "A Hybrid Recursive Multi-Way
    Number Partitioning Algorithm"
Paper from Richard E. Korf,
Paper link:
    http://citeseerx.ist.psu.edu/viewdoc/download?rep=rep1&type=pdf&doi=10.1.1.208.2132

My Summary of the paper (Hebrew):
    https://github.com/kggold4/programming-research-algorithms-assignments/blob/main/Research/Ex1/%D7%A1%D7%99%D7%9B%D7%95%D7%9D%20%D7%9E%D7%90%D7%9E%D7%A8.pdf
"""


def greedy_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Greedy Algorithm (GA)
    Partition the numbers using the greedy number partitioning algorithm
    https://en.wikipedia.org/wiki/Greedy_number_partitioning
    Algorithm number in Paper 2.1

    >>> greedy_algorithm(items=[1, 2, 3, 3, 5, 9, 9], k=2)
    [9, 5, 2], sum=16.0
    [9, 3, 3, 1], sum=16.0

    >>> greedy_algorithm(items=[4, 5, 6, 7, 8], k=3)
    [8], sum=8.0
    [7, 4], sum=11.0
    [6, 5], sum=11.0

    >>> greedy_algorithm(items=[1, 2, 3, 3, 5, 9, 9], k=3)
    [9, 2], sum=11.0
    [9, 1], sum=10.0
    [5, 3, 3], sum=11.0

    """
    pass


def complete_greedy_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Complete Greedy Algorithm (CGA)
    Partition the numbers using the Complete Greedy number partitioning algorithm (Korf, 1995):
    https://en.wikipedia.org/wiki/Greedy_number_partitioning
    Algorithm number in Paper 2.1

    >>> complete_greedy_algorithm(items=[4,5,6,7,8], k=2)
    [6, 5, 4], sum=15.0
    [8, 7], sum=15.0

    >>> complete_greedy_algorithm(items=[46, 39, 27, 26, 16, 13, 10], k=3)
    [27, 26, 10], sum=63.0
    [39, 16], sum=55.0
    [46, 13], sum=59.0

    """
    pass


def heuristic_karmarkar_karp_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Heuristic Karmarkar Karp Algorithm (KK)
    Taken help from:
    https://github.com/fuglede/numberpartitioning/blob/24803bd5be58e6c76f6fc3dbe187cd2d9c0995dd/tests/test_karmarkar_karp.py
    and from:
    https://github.com/arzieg/karmarkar/blob/4506d5adf22c5d7347ac3c30edef292de06e4255/kk.py
    Algorithm number in Paper 2.2

    >>> heuristic_karmarkar_karp_algorithm(items=[1, 6, 2, 3, 4, 1, 7, 6, 4], k=2)
    [4, 7, 6], sum=17
    [1, 2, 1, 3, 4, 6], sum=17

    >>> heuristic_karmarkar_karp_algorithm(items=[18, 17, 12, 11, 8, 2], k=2)
    [8, 11, 17], sum=36
    [12, 18, 2], sum=32

    >>> heuristic_karmarkar_karp_algorithm(items=[4, 5, 6, 7, 8], k=3)
    [8], sum=8.0
    [4, 7], sum=11.0
    [5, 6], sum=11.0

    """
    pass


def complete_heuristic_karmarkar_karp_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Complete Heuristic Karmarkar Karp Algorithm (CKK)
    Taken help from:
    https://github.com/fuglede/numberpartitioning/blob/24803bd5be58e6c76f6fc3dbe187cd2d9c0995dd/tests/test_complete_karmarkar_karp.py
    and from:
    https://github.com/arzieg/karmarkar/blob/4506d5adf22c5d7347ac3c30edef292de06e4255/ckk.py
    Algorithm number in Paper 2.3

    >>> complete_heuristic_karmarkar_karp_algorithm(items=[1, 6, 2, 3, 4, 1, 7, 6, 4], k=2)
    [4, 7, 6], sum=17.0
    [1, 2, 1, 3, 4, 6], sum=17.0

    >>> complete_heuristic_karmarkar_karp_algorithm(items=[95, 15, 75, 25, 85, 5], k=2)
    [75, 85], sum=163.0
    [5, 95, 15, 25], sum=140.0

    >>> complete_heuristic_karmarkar_karp_algorithm(items=[5, 8, 6, 4, 7], k=3)
    [4, 7], sum=11.0
    [5, 6], sum=11.0
    [8], sum=8.0

    """
    pass


def recursive_number_partitioning_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Recursive Number Partitioning Algorithm (RNP)
    Algorithm number in Paper 2.5

    >>> recursive_number_partitioning_algorithm(items=[1, 6, 2, 3, 4, 1, 7, 6, 4], k=2)
    [4, 7, 6], sum=17.0
    [1, 2, 1, 3, 4, 6], sum=17.0

    >>> recursive_number_partitioning_algorithm(items=[18, 17, 12, 11, 8, 2], k=2)
    [8, 11, 17], sum=36.0
    [12, 18, 2], sum=32.0

    >>> recursive_number_partitioning_algorithm(items=[95, 15, 75, 25, 85, 5], k=2)
    [75, 85], sum=163.0
    [5, 95, 15, 25], sum=140.0

    >>> numbers = [4, 5, 6, 7, 8]
    >>> recursive_number_partitioning_algorithm(items=numbers, k=3)
    [8], sum=8.0
    [4, 7], sum=11.0
    [5, 6], sum=11.0
    """
    pass


def improved_recursive_number_partitioning_algorithm(items: list[int], k: int) -> (list[list[int]]):
    """
    Improved Recursive Number Partitioning Algorithm (IRNP)
    Algorithm number in Paper 3.0

    >>> improved_recursive_number_partitioning_algorithm(items=[18, 17, 12, 11, 8, 2], k=2)
    [17, 11, 8], sum=36.0
    [18, 12, 2], sum=32.0

    >>> improved_recursive_number_partitioning_algorithm(items=[95, 15, 75, 25, 85, 5], k=2)
    [75, 85], sum=163.0
    [5, 95, 15, 25], sum=140.0

    >>> improved_recursive_number_partitioning_algorithm(items=[5, 8, 6, 4, 7], k=3)
    [4, 7], sum=11.0
    [5, 6], sum=11.0
    [8], sum=8.0

    >>> improved_recursive_number_partitioning_algorithm(items=[4, 5, 6, 7, 8], k=3)
    [4, 7], sum=11.0
    [5, 6], sum=11.0
    [8], sum=8.0

    """
    pass


if __name__ == '__main__':
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print(f"{failures} failures, {tests} tests")
