import random
import unittest
import numpy as np
from unittest import TestCase

from algorithms import greedy_algorithm, complete_greedy_algorithm, heuristic_karmarkar_karp_algorithm, \
    complete_heuristic_karmarkar_karp_algorithm, recursive_number_partitioning_algorithm, \
    improved_recursive_number_partitioning_algorithm

MAX_VALUE_1 = 1000
MAX_VALUE_2 = 10000
MAX_VALUE_3 = 100000


class TestAlgorithms(TestCase):
    """
    Test cases for all the algorithms at algorithms.py
    """
    def test_base_greedy_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_greedy_algorithm(self):
        numbers = [1, 2, 3, 3, 5, 9, 9]
        k = 2
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[9, 5, 2])
        assert sum(results[0]) == 16
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[9, 3, 3, 1])
        assert sum(results[1]) == 16

        numbers = [4, 5, 6, 7, 8]
        k = 3
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8])
        assert sum(results[0]) == 8
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[7, 4])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[6, 5])
        assert sum(results[2]) == 11

        numbers = [1, 2, 3, 3, 5, 9, 9]
        k = 3
        results = greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[9, 2])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[9, 1])
        assert sum(results[1]) == 10
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[5, 3, 3])
        assert sum(results[2]) == 11

    def test_base_complete_greedy_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = complete_greedy_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = complete_greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = complete_greedy_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_complete_greedy_algorithm(self):
        numbers = [4, 5, 6, 7, 8]
        k = 2
        results = complete_greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[6, 5, 4])
        assert sum(results[0]) == 15
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[8, 7])
        assert sum(results[1]) == 15

        numbers = [46, 39, 27, 26, 16, 13, 10]
        k = 3
        results = complete_greedy_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[27, 26, 10])
        assert sum(results[0]) == 63
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[39, 16])
        assert sum(results[1]) == 55
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[46, 13])
        assert sum(results[2]) == 59

    def test_base_heuristic_karmarkar_karp_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_heuristic_karmarkar_karp_algorithm(self):
        numbers = [1, 6, 2, 3, 4, 1, 7, 6, 4]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7, 6])
        assert sum(results[0]) == 17
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[1, 2, 1, 3, 4, 6])
        assert sum(results[1]) == 17

        numbers = [18, 17, 12, 11, 8, 2]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8, 11, 17])
        assert sum(results[0]) == 36
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[12, 18, 2])
        assert sum(results[1]) == 32

        numbers = [1, 10, 10, 1]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[1, 10])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[10, 1])
        assert sum(results[1]) == 11

        numbers = [95, 15, 75, 25, 85, 5]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[75, 85])
        assert sum(results[0]) == 163
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 95, 15, 25])
        assert sum(results[1]) == 140

        numbers = [8, 7, 6, 5, 4]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 5, 7])
        assert sum(results[0]) == 16
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[6, 8])
        assert sum(results[1]) == 14

        numbers = [4, 5, 6, 7, 8]
        k = 3
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8])
        assert sum(results[0]) == 8
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[4, 7])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[5, 6])
        assert sum(results[2]) == 11

    def test_base_complete_heuristic_karmarkar_karp_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = complete_heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = complete_heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = complete_heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_complete_heuristic_karmarkar_karp_algorithm(self):
        numbers = [5, 8, 6, 4, 7]
        k = 3
        results = complete_heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 6])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[8])
        assert sum(results[2]) == 8

        numbers = [4, 5, 6, 7, 8]
        k = 3
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8])
        assert sum(results[0]) == 8
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[4, 7])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[5, 6])
        assert sum(results[2]) == 11

        numbers = [1, 6, 2, 3, 4, 1, 7, 6, 4]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7, 6])
        assert sum(results[0]) == 17
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[1, 2, 1, 3, 4, 6])
        assert sum(results[1]) == 17

        numbers = [18, 17, 12, 11, 8, 2]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8, 11, 17])
        assert sum(results[0]) == 36
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[12, 18, 2])
        assert sum(results[1]) == 32

        numbers = [1, 10, 10, 1]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[1, 10])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[10, 1])
        assert sum(results[1]) == 11

        numbers = [95, 15, 75, 25, 85, 5]
        k = 2
        results = heuristic_karmarkar_karp_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[75, 85])
        assert sum(results[0]) == 163
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 95, 15, 25])
        assert sum(results[1]) == 140

    def test_base_recursive_number_partitioning_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_recursive_number_partitioning_algorithm(self):
        numbers = [5, 8, 6, 4, 7]
        k = 3
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 6])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[8])
        assert sum(results[2]) == 8

        numbers = [4, 5, 6, 7, 8]
        k = 3
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8])
        assert sum(results[0]) == 8
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[4, 7])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[5, 6])
        assert sum(results[2]) == 11

        numbers = [1, 6, 2, 3, 4, 1, 7, 6, 4]
        k = 2
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7, 6])
        assert sum(results[0]) == 17
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[1, 2, 1, 3, 4, 6])
        assert sum(results[1]) == 17

        numbers = [18, 17, 12, 11, 8, 2]
        k = 2
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8, 11, 17])
        assert sum(results[0]) == 36
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[12, 18, 2])
        assert sum(results[1]) == 32

        numbers = [1, 10, 10, 1]
        k = 2
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[1, 10])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[10, 1])
        assert sum(results[1]) == 11

        numbers = [95, 15, 75, 25, 85, 5]
        k = 2
        results = recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[75, 85])
        assert sum(results[0]) == 163
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 95, 15, 25])
        assert sum(results[1]) == 140

    def test_base_improved_recursive_number_partitioning_algorithm(self):
        numbers = []
        k = random.randint(0, MAX_VALUE_1)
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == 0

        numbers = list(np.arange(1, 10))
        k = 9
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        for i in numbers:
            unittest.TestCase.assertCountEqual(self=self, first=results[i - 1], second=[i])

        numbers = [random.randint(0, MAX_VALUE_2) for _ in range(random.randint(0, MAX_VALUE_3))]
        k = 0
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == 0

    def test_improved_recursive_number_partitioning_algorithm(self):
        numbers = [5, 8, 6, 4, 7]
        k = 3
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 6])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[8])
        assert sum(results[2]) == 8

        numbers = [4, 5, 6, 7, 8]
        k = 3
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8])
        assert sum(results[0]) == 8
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[4, 7])
        assert sum(results[1]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[2], second=[5, 6])
        assert sum(results[2]) == 11

        numbers = [1, 6, 2, 3, 4, 1, 7, 6, 4]
        k = 2
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[4, 7, 6])
        assert sum(results[0]) == 17
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[1, 2, 1, 3, 4, 6])
        assert sum(results[1]) == 17

        numbers = [18, 17, 12, 11, 8, 2]
        k = 2
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[8, 11, 17])
        assert sum(results[0]) == 36
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[12, 18, 2])
        assert sum(results[1]) == 32

        numbers = [1, 10, 10, 1]
        k = 2
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[1, 10])
        assert sum(results[0]) == 11
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[10, 1])
        assert sum(results[1]) == 11

        numbers = [95, 15, 75, 25, 85, 5]
        k = 2
        results = improved_recursive_number_partitioning_algorithm(items=numbers, k=k)
        assert len(results) == k
        unittest.TestCase.assertCountEqual(self=self, first=results[0], second=[75, 85])
        assert sum(results[0]) == 163
        unittest.TestCase.assertCountEqual(self=self, first=results[1], second=[5, 95, 15, 25])
        assert sum(results[1]) == 140
