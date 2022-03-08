import random
import string
from unittest import TestCase
import q2

RANGE_LOOP_1 = 10
RANGE_LOOP_2 = 100
RANGE_LOOP_3 = 1000
RANGE_LOOP_4 = 10000


# help from https://www.javatpoint.com/python-program-to-generate-a-random-string
def generate_random_string(length: int):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


@q2.last_call
def f(x: int):
    return x ** 2


@q2.last_call
def g(s: str):
    return s + "-string"


@q2.last_call
def q(x):
    return True


class Test(TestCase):
    def test_last_call_f_random_values(self):
        q2.reset_last_value()
        last_value = None
        for _ in range(RANGE_LOOP_2):
            random_int = random.randint(0, RANGE_LOOP_1)
            print(random_int)
            if last_value is None and random_int != last_value:
                assert f(random_int) == random_int ** 2  # first time

            print(f(random_int))
            for _ in range(RANGE_LOOP_1):
                assert f(random_int) == f"I already told you the the answer is {random_int ** 2}!"
            last_value = random_int

    def test_last_call_g_random_values(self):
        q2.reset_last_value()
        last_value = None
        for _ in range(RANGE_LOOP_2):
            random_word = generate_random_string(length=RANGE_LOOP_1)
            print(random_word)
            if last_value is None and random_word != last_value:
                assert g(random_word) == random_word + "-string"  # first time

            print(g(random_word))
            for _ in range(RANGE_LOOP_1):
                assert g(random_word) == f"I already told you the the answer is {random_word}-string!"
            last_value = random_word

    def test_last_call_q(self):
        q2.reset_last_value()
        assert q(15) is True  # first time
        for _ in range(RANGE_LOOP_1):
            assert q(15) == "I already told you the the answer is True!"

        assert q('3') is True  # first time
        for _ in range(RANGE_LOOP_1):
            assert q('3') == "I already told you the the answer is True!"

        assert q(False) is True  # first time
        for _ in range(RANGE_LOOP_1):
            assert q(False) == "I already told you the the answer is True!"

    def test_last_case_special_cases(self):
        q2.reset_last_value()
        # 0 and False assertion is equal to True: 0 == False -> True
        assert q(False) is True
        try:
            assert q(0) is True
            assert False
        except AssertionError:
            assert True

        for _ in range(RANGE_LOOP_1):
            assert q(0) == "I already told you the the answer is True!"

        # not arguments
        try:
            assert q() is True
            assert False
        except TypeError:
            assert True
