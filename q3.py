EPSILON = 0.0001
DEFAULT_ITERATIONS = 10


# take help from: https://personal.math.ubc.ca/~pwalls/math-python/differentiation/differentiation/
def derivative(func, x, h: float = EPSILON):
    return (func(x + h) - func(x)) / h


def find_root(func, low, high, iterations: int = DEFAULT_ITERATIONS):
    if high < low:
        # swap
        temp = low
        low = high
        high = temp

    xn = low
    step = (high - low) / iterations  # step each iteration
    while low <= high:
        low += step
        xn_value = func(xn)

        # found approximately solution with epsilon
        if abs(xn_value) < EPSILON:
            return float("{:.4f}".format(xn))

        derivative_value = derivative(func, xn)
        if derivative_value == 0:
            print('No solution found')
            return None

        # calculate next xn
        xn = xn - xn_value / derivative_value

    print('No solution found')
    return None


if __name__ == '__main__':
    print(find_root(lambda x: x**2 - 4, 1, 3))
