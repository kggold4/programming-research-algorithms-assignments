from unittest import TestCase

from q1 import safe_call


def f1(x: int, y: float, z):
    return x + y + z


def f2(x: int, y: float, z):
    return x * y * z


class Test(TestCase):
    def test_safe_call_1(self):
        # f1 function
        assert safe_call(f1, x=5, y=7.0, z=3) == 15.0
        assert safe_call(f1, x=15, y=7.2, z=6) == 28.2

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

        # f2 function
        assert safe_call(f2, x=5, y=7.0, z=3) == 105.0
        assert safe_call(f2, x=15, y=7.2, z=6) == 648.0

        # cannot perform y: int, raise TypeError
        try:
            safe_call(f2, x=0, y=0, z=0)
            assert False
        except TypeError:
            assert True

        # cannot perform y: int, raise TypeError
        try:
            safe_call(f2, x=0, y=0, z='a')
            assert False
        except TypeError:
            assert True

        # cannot perform x: float, raise TypeError
        try:
            safe_call(f2, x=0.1, y=0.0, z=0)
            assert False
        except TypeError:
            assert True

        # cannot operate (int or float) + str, raise TypeError
        try:
            safe_call(f2, x=4, y=5.0, z='a')
            assert False
        except TypeError:
            assert True
