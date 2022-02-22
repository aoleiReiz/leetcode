from functools import wraps

def decrator(fn):
    """decrator"""
    @wraps(fn)
    def inner(*args, **kwargs):
        """inner"""
        fn(*args, **kwargs)
    return inner

@decrator
def f():
    """func f"""
    print(f.__doc__)
    print("funcf")


f()

