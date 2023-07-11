
print(f"Hello, i'm module {__name__}")

var1 = 1000

def some_cool_function():
    return 'I do nothing'
    
def func(a: str, b: str):
    return f"{a.capitalize()} {b.upper()}"

if __name__ == "__main__":
    print(f"{some_cool_function.__name__} :: {some_cool_function()}")
    print(f"{func.__name__} :: {func('run', 'func')}")
