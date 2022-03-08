import random
from unittest import TestCase

import q3

ARRAY_LENGTH_1 = 10
ARRAY_LENGTH_2 = 100
ARRAY_LENGTH_3 = 1000
ARRAY_LENGTH_4 = 10000


def get_random_list(length: int = None, maximum: int = ARRAY_LENGTH_4):
    if length is None:
        length = random.randint(0, ARRAY_LENGTH_2)
    return [random.randint(0, maximum) for _ in range(length)]


class TestList(TestCase):
    def test_list_functions_base_cases_sort(self):
        base_list = [i for i in range(ARRAY_LENGTH_3)]
        random.shuffle(base_list)
        new_list = q3.List(base_list)
        sorted(base_list)
        sorted(new_list)
        assert base_list == new_list

    def test_list_functions_base_cases_append(self):
        base_list = q3.List(get_random_list())
        current_len = len(base_list)
        random_number = random.randint(ARRAY_LENGTH_3, ARRAY_LENGTH_4)
        base_list.append(random_number)
        assert random_number in base_list
        assert current_len + 1 == len(base_list)

    def test_list_functions_base_cases_clear(self):
        base_list = q3.List(get_random_list())
        base_list.clear()
        assert len(base_list) == 0
        assert base_list == []

    def test_list_functions_base_cases_remove(self):
        base_list = q3.List([i for i in range(ARRAY_LENGTH_3)])
        current_len = len(base_list)
        random_choice = random.choice(base_list)
        base_list.remove(random_choice)
        assert random_choice not in base_list
        assert current_len - 1 == len(base_list)

    def test_list_base_cases(self):
        my_list1 = q3.List([1, [2, [3, 4]]])
        assert my_list1[1, 1, 1] == 4

        my_list2 = q3.List([1, 2, 3, [5, 6]])
        my_list2.append(8)
        assert my_list2[3, 1] == 6

        my_list3 = q3.List([1, [1, [1, [1]]]])
        assert my_list3[1, 1, 1, 0] == 1
