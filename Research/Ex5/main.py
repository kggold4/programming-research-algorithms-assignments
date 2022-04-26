from typing import Callable

from algorithms import complete_greedy_algorithm, heuristic_karmarkar_karp_algorithm, \
    recursive_number_partitioning_algorithm


def partition(algorithm: Callable, items: list[int], k: int):
    """
    Base Partitions Cases:
    >>> partition(algorithm=complete_greedy_algorithm, items=[46, 39, 27, 26, 16, 13, 10], k=3)
    [27, 26, 10], sum=63
    [39, 16], sum=55
    [46, 13], sum=59

    >>> partition(algorithm=heuristic_karmarkar_karp_algorithm, items=[18, 17, 12, 11, 8, 2], k=2)
    [8, 11, 17], sum=36
    [12, 18, 2], sum=32

    >>> partition(algorithm=recursive_number_partitioning_algorithm, items=[1, 6, 2, 3, 4, 1, 7, 6, 4], k=2)
    [4, 7, 6], sum=17
    [1, 2, 1, 3, 4, 6], sum=17

    """
    return algorithm(items, k)


def main():
    # example:
    partition(algorithm=complete_greedy_algorithm, items=[1, 2, 3, 4], k=2)


if __name__ == '__main__':
    main()
