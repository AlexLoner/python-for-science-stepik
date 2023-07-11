# test_module2

def some_cool_function():
    print('I do nothing')


def func(a: str, b: str):
    return f"{a.capitalize()} {b.upper()}"


def prod(a=1, *args):
    for i in args:
        a *= i
    return a
