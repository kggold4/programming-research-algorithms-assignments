def safe_call(func, **kwargs):
    for key, value in kwargs.items():
        # check if the key has an annotation in the function, continue if not
        try:
            required_type = func.__annotations__[key]
        except KeyError:
            continue

        # key has an annotation in the function, check if it match the value
        else:
            real_type = type(value)
            if required_type != real_type:
                raise TypeError(
                    f"Argument {key} with value of {value} should be {required_type} type and not {real_type}")
    try:
        print(func(**kwargs))
    except Exception as e:
        print(f"Exception while call given function {func.__name__}")
        raise e


# example
def f(x: int, y: float, z):
    return x + y + z


if __name__ == '__main__':
    safe_call(f, x=5, y=7.0, z=3)
