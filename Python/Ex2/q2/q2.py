# global last value
# last_value = None


class LastCall:
    def __init__(self):
        self.last_call = None

    def last_call_value(self, value):
        self.last_call = value


# def reset_last_value():
    # global last_value
    # last_value = None


def last_call(func):
    last_call_value = LastCall()

    def inner(arg):
        if not (last_call_value.last_call is None or arg != last_value):
            result = f"I already told you the the answer is {func(arg)}!"
            print(result)
            return result
        else:
            last_call_value.last_call_value(arg)
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
