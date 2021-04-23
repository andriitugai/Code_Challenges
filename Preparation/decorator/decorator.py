import time
from datetime import datetime


def my_decor(func):
    def inner(*args, **kwargs):
        t0 = datetime.now()
        result = func(*args, **kwargs)
        t1 = datetime.now()
        print(f"Function [{func.__name__}] called. Time elapsed: {t1-t0}.")
        return result

    return inner


@my_decor
def hello(name):
    print(f"Hello {name}!")
    time.sleep(4)


if __name__ == '__main__':
    hello("Andrii")
