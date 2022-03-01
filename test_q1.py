from unittest import TestCase

from q1 import safe_call


def f0():
    return 10


def f1(x: int, y: float, z):
    return x + y + z


def f2(x: int, y: float, z):
    return x * y * z


def f3(x: int, y: int, z: int, w: int):
    return (x + y) ** z - w


def f4(a, b, c):
    return (a + b) * c


def f5(x: int, y: int, z):
    return x * y * z


def f6(x: int, y: int, z):
    return x * y * z


def f7(x: int = 5, y: int = 6, z: int = 10):
    return x * y * z


def f8(x: int = 5, y: int = 6, z: int = 10):
    return x * y / z


class Test(TestCase):

    def test_basic_cases_1(self):
        assert safe_call(f1, x=5, y=7.0, z=3) == 15.0
        assert safe_call(f1, x=15, y=7.2, z=6) == 28.2
        assert safe_call(f1, x=89, y=1.1111434289, z=17) == 107.1111434289
        assert safe_call(f2, x=5, y=7.0, z=3) == 105.0
        assert safe_call(f4, a=2, b=4, c=False) == 0
        assert safe_call(f4, a=False, b=True, c=True) == True
        assert safe_call(f4, a=False, b=True, c=True) is not True
        assert safe_call(f4, a=False, b=True, c=True) == 1

    def test_basic_cases_2(self):
        assert safe_call(f5, x=5, y=7, z='a') == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        assert safe_call(f5, x=0, y=1, z='a') == ''
        assert safe_call(f5, x=10, y=0, z='asd') == ''
        assert safe_call(f5, x=2, y=2, z='ab') == 'abababab'
        assert safe_call(f5, x=5, y=7, z=0) == 0
        assert safe_call(f5, x=5, y=7, z=1.2) == 42.0
        assert safe_call(f5, x=50, y=2, z=1.1111) == 111.11
        assert safe_call(f4, a=5, b=5, c='c') == 'cccccccccc'

    def test_wrong_number_of_arguments(self):
        # less arguments than should
        try:
            safe_call(f1, x=5, y=5.5)
            assert False
        except TypeError:
            assert True

        # more arguments than should
        try:
            safe_call(f1, x=5, y=5.0, z=5, w=3)
            assert False
        except TypeError:
            assert True

        # expected non arguments
        try:
            safe_call(f0, x=1)
            assert False
        except TypeError:
            assert True

        # expected non arguments
        try:
            safe_call(f0, x=1, y=5)
            assert False
        except TypeError:
            assert True

    def test_wrong_arguments_names(self):
        # wrong name of argument
        try:
            safe_call(f7, w=5)
            assert False
        except TypeError:
            assert True

        # wrong name of argument
        try:
            safe_call(f1, x=1, y=2.23, z=3, w=5)
            assert False
        except TypeError:
            assert True

    def test_wrong_argument_types_1(self):
        # cannot perform y: int, raise TypeError
        try:
            safe_call(f1, x=1, y=0, z=0)
            assert False
        except TypeError:
            assert True

        # cannot perform y: int, raise TypeError
        try:
            safe_call(f1, x=1, y=0, z='a')
            assert False
        except TypeError:
            assert True

        # cannot perform x: float, raise TypeError
        try:
            safe_call(f1, x=0.1, y=0.0, z=2)
            assert False
        except TypeError:
            assert True

        # cannot operate (int or float) + str, raise TypeError
        try:
            safe_call(f1, x=4, y=5.0, z='a')
            assert False
        except TypeError:
            assert True

        # cannot multiple float and string
        try:
            safe_call(f2, x=5, y=7.0, z='a')
            assert False
        except TypeError:
            assert True

    def test_function_error(self):
        try:
            safe_call(f8, z=0)
            assert False
        except ZeroDivisionError:
            assert True

    def test_special_cases(self):
        # function with default arguments
        assert safe_call(f7) == 300
        assert safe_call(f7, z=0) == 0
        assert safe_call(f7, z=10) == 300
        assert safe_call(f7, z=5) == 150
        assert safe_call(f7, x=3, y=2, z=5) == 30
