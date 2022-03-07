# global last value
last_value = None


def last_call(func):
    def inner(arg):
        global last_value
        if not (last_value is None or arg != last_value):
            print(f"I already told you the the answer is {func(arg)}!")
        else:
            last_value = arg
        return func(arg)

    return inner


# example

@last_call
def f(x: int):
    return x ** 2


@last_call
def g(s: str):
    return s + "-string"


if __name__ == '__main__':
    f(2)
    f(2)
    f(2)
    f(2)
    f(3)
    f(3)
    g("hello")
    g("hello")
