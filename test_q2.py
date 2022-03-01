import random
from unittest import TestCase

from q2 import print_sorted

MAX_1 = 100
MAX_2 = 10000
MAX_3 = 10000000
MAX_4 = 1


class Test(TestCase):
    def test_base_cases_list_1level(self):
        # int arrays
        random_array_1 = [i for i in range(random.randint(0, MAX_1))]
        assert print_sorted(random_array_1) == sorted(random_array_1)
        random_array_2 = [i for i in range(random.randint(0, MAX_2))]
        assert print_sorted(random_array_2) == sorted(random_array_2)
        random_array_3 = [i for i in range(random.randint(0, MAX_3))]
        assert print_sorted(random_array_3) == sorted(random_array_3)
        random_array_4 = [i for i in range(random.randint(0, 0))]
        assert print_sorted(random_array_4) == sorted(random_array_4)

        # float arrays
        random_array_5 = [random.random() for _ in range(random.randint(0, MAX_4))]
        assert print_sorted(random_array_5) == sorted(random_array_5)

        # string arrays
        assert print_sorted(['a', 'c', 'b', 'e', 'd']) == ['a', 'b', 'c', 'd', 'e']

    def test_base_cases_list_2level(self):
        assert print_sorted([2, 1, [7, 6], 4, [6, 5], 3]) == [1, 2, 3, 4, [5, 6], [6, 7]]
        assert print_sorted([1, 2, [6, 7], 3, [5, 6], 4]) == [1, 2, 3, 4, [5, 6], [6, 7]]
        assert print_sorted([[6, 7], 1, 2, [5, 6], 4, 3]) == [1, 2, 3, 4, [5, 6], [6, 7]]
        assert print_sorted([[6, 7], [5, 6], 1, 3, 4, 2]) == [1, 2, 3, 4, [5, 6], [6, 7]]
        assert print_sorted([4, 3, 2, 1, [6, 7], [5, 6]]) == [1, 2, 3, 4, [5, 6], [6, 7]]
        assert print_sorted([3, 2, 1, [6, 7], [5, 6], 4]) == [1, 2, 3, 4, [5, 6], [6, 7]]

    def test_base_cases_dict_1level(self):
        # random 1 level dict
        random_keys = [i for i in range(MAX_1)]
        random.shuffle(random_keys)
        random_values = [i for i in range(MAX_1)]
        random_dict = dict(zip(random_keys,
                               random_values))  # help: https://www.kite.com/python/answers/how-to-create-a-dictionary-from-two-lists-in-python
        assert print_sorted(random_dict) == {k: v for k, v in sorted(random_dict.items(), key=lambda item: item[
            1])}  # help: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

    def test_base_cases_dict_2level(self):
        assert print_sorted({'b': 1, 'a': [5, 3]}) == {'a': [3, 5], 'b': 1}
        assert print_sorted({2: 1, 1: [5, 3]}) == {1: [3, 5], 2: 1}

    def test_base_cases_tuple_1level(self):
        assert print_sorted((9, 8, 7, 6, 5, 4, 3, 2, 1)) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
        assert print_sorted(1) == 1
        assert print_sorted(data=tuple()) == ()
        assert print_sorted((1, 0)) == (0, 1)
        assert print_sorted(('b', 'a', 'c')) == ('a', 'b', 'c')

    def test_base_cases_tuple_2level(self):
        assert print_sorted(([9, 8, 5, 7], 5, 4, [0], [2, 3, 1], 6, 2, [1, 0])) == (2, 4, 5, 6, [0], [0, 1], [1, 2, 3], [5, 7, 8, 9])
        assert print_sorted(([6, 5], [4, 3], [8, 7], [2, 1])) == ([1, 2], [3, 4], [5, 6], [7, 8])

        # random 2 level tuple
        random_arr = [i for i in range(MAX_2)]
        random.shuffle(random_arr)
        assert print_sorted(tuple(random_arr)) == tuple(sorted(random_arr))

    def test_base_cases_set(self):
        assert print_sorted(
            {frozenset([9, 8, 5, 7]), 5, 4, frozenset([0]), frozenset([2, 3, 1]), 6, 2, frozenset([1, 0])}) == {2, 4, 5,
                                                                                                                6,
                                                                                                                frozenset(
                                                                                                                    {0,
                                                                                                                     1}),
                                                                                                                frozenset(
                                                                                                                    {8,
                                                                                                                     9,
                                                                                                                     5,
                                                                                                                     7}),
                                                                                                                frozenset(
                                                                                                                    {1,
                                                                                                                     2,
                                                                                                                     3}),
                                                                                                                frozenset(
                                                                                                                    {
                                                                                                                        0})}
