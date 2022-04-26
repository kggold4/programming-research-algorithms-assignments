def test_function(s):
    """
    >>> test_function("a")
    a
    """
    print(s)

if __name__ == '__main__':
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print(f"{failures} failures, {tests} tests")