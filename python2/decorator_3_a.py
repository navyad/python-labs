def outer(some_func):
    def inner(a, b):
        return some_func(a, b)
    inner.__name__ = some_func.__name__
    inner.__doc__ = some_func.__doc__
    return inner


@outer
def add(x, y):
    """adds a x and y"""
    return x + y

if __name__ == '__main__':
    print add.__name__

