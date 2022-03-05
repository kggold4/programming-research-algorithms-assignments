import random
from unittest import TestCase

from q3 import find_root
import numpy as np

EPSILON = 0.001
ITERATIONS_1 = 10
ITERATIONS_2 = 100
ITERATIONS_3 = 1000


def close_by_epsilon(a, b, epsilon: float = EPSILON):
    return abs(a - b) < epsilon


class Test(TestCase):
    def test_find_root_base_functions(self):
        assert find_root(lambda x: x ** 2 - 4, 1, 3, iterations=ITERATIONS_1) == 2
        assert close_by_epsilon(find_root(lambda x: x ** 2, 0, 1, iterations=ITERATIONS_1), 0.0)
        assert close_by_epsilon(find_root(lambda x: x ** 2 - 2, 1, 3, iterations=ITERATIONS_1), np.sqrt(2))
        assert close_by_epsilon(find_root(lambda x: x ** 2 - 5, 1, 3, iterations=ITERATIONS_1), np.sqrt(5))
        assert close_by_epsilon(find_root(lambda x: x ** 2 - 16, 1, 10, iterations=ITERATIONS_2), np.sqrt(16))
        assert close_by_epsilon(find_root(lambda x: x ** 2 - 524524, 0, ITERATIONS_3, iterations=ITERATIONS_3),
                                np.sqrt(524524))

    def test_find_root_random(self):
        n1 = random.randint(1, ITERATIONS_1)
        assert close_by_epsilon(
            find_root(lambda x: x ** 2 - n1, 1, np.ceil(np.sqrt(ITERATIONS_1)), iterations=ITERATIONS_1), np.sqrt(n1))

        n2 = random.randint(1, ITERATIONS_2)
        assert close_by_epsilon(
            find_root(lambda x: x ** 2 - n2, 1, np.ceil(np.sqrt(ITERATIONS_2)), iterations=ITERATIONS_2), np.sqrt(n2))

        n3 = random.randint(1, ITERATIONS_3)
        assert close_by_epsilon(
            find_root(lambda x: x ** 2 - n3, 1, np.ceil(np.sqrt(ITERATIONS_3)), iterations=ITERATIONS_3), np.sqrt(n3))

    def test_find_root_wrong_input(self):
        # wrong range
        assert find_root(lambda x: x ** 2 - 4, 0, 1) is None
        assert find_root(lambda x: x ** 2 - 16, 0, 1) is None
        assert find_root(lambda x: x ** 2, 9, 10) is None
        assert find_root(lambda x: x ** 2, 10, 9) is None

        # opposite range
        assert find_root(lambda x: x ** 2, 0, 1) is not None
        assert find_root(lambda x: x ** 2, 1, 0) is None

    def test_find_root_special_functions(self):
        assert close_by_epsilon(find_root(lambda x: x ** 3, 0, 4, iterations=ITERATIONS_1), 0.0)
