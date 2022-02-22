from functools import wraps


def timed(reps=5):
    def outer(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            for _ in range(reps):
                fn(*args, **kwargs)
        return inner
    return outer

@timed(6)
def f(a):
    print(a)

f(3)
f(5)