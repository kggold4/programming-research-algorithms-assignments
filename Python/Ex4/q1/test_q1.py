import random
import unittest
from unittest import TestCase

import q1

TIMES_TO_TRY_10 = 10


class TestBoundedSubsets(TestCase):
    def test_base_list_set_tests(self):
        base_list = random.choice([[1, 2, 3], {1, 2, 3}])
        max_sum = 4
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[3])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 3])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_list_set_tests(self):
        base_list = random.choice([[6, 7, 100], {6, 7, 100}])
        max_sum = 106
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[6])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[7])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[100])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[6, 7])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[6, 100])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_second_list_set_tests(self):
        r = random.randint(2, 1000000)
        base_list = [1, r]
        max_sum = r
        print(r)
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[r])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_unsorted_base_values_list_set_cases(self):
        base_list = random.choice([[3, 1, 2], {3, 1, 2}])
        max_sum = 4
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[3])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 3])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_unsorted_values_list_set_cases(self):
        base_list = [i for i in range(1, 10)]
        random.shuffle(base_list)
        max_sum = 5
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[3])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[4])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[5])

        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 3])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 4])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2, 3])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_big_base_list(self):
        base_list = [i for i in range(1, 20)]
        random.shuffle(base_list)
        max_sum = 10000000000
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        for subset in bounded_subsets.subsets:
            unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=subset)

    def test_value_error_list_cases(self):
        max_sum = 0

        base_list = [i for i in range(0, 10)]
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = [1, 2, 3, 4, 5, "a"]
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = [1, 2, 3, 4, 5, '']
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = [1, 2, 3, 4, 5, False, True]
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

    def test_value_error_set_cases(self):
        max_sum = 0

        base_list = {i for i in range(0, 10)}
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = {1, 2, 3, 4, 5, "a"}
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = {1, 2, 3, 4, 5, ''}
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = {1, 2, 3, 4, 5, False, True}
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

    def test_special_empty_list_case(self):
        base_list = []
        max_sum = 20
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_special_zero_bound_case(self):
        base_list = [i for i in range(100)]
        max_sum = 0
        # unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        for _ in range(TIMES_TO_TRY_10):
            try:
                bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
                self.assert_(False)
            except ValueError:
                self.assert_(True)

    def test_special_one_bound_case(self):
        base_list = [1, 2]
        max_sum = 1
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_special_big_bound_case(self):
        base_list = [i for i in range(1, 3)]
        max_sum = 100
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        print(bounded_subsets)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 2])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)

    def test_special_negative_values_cases(self):
        base_list = [1, 2, -3]
        max_sum = 2
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = [1, 2, 3]
        max_sum = -1
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

    def test_special_zero_values_cases(self):
        base_list = [1, 2, 0]
        max_sum = 5
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

        base_list = [1, 2, 3]
        max_sum = 0
        try:
            bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
            self.assert_(False)
        except ValueError:
            self.assert_(True)

    def test_duplicates_cases(self):
        base_list = random.choice(
            [[1, 2, 3, 3, 1, 1, 1, 2, 3, 2, 1, 1, 2, 2, 3, 3], {1, 2, 3, 3, 1, 1, 1, 2, 3, 2, 1, 1, 2, 2, 3, 3}])
        max_sum = 4
        bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[3])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 2])
        unittest.TestCase.assertCountEqual(self=self, first=next(bounded_subsets), second=[1, 3])
        for _ in range(TIMES_TO_TRY_10):
            try:
                self.assert_(next(bounded_subsets), None)
                self.assert_(False)
            except StopIteration:
                self.assert_(True)
