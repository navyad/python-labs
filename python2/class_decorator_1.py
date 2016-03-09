import functools


class outer(object):
    def __init__(self, some_func):
        self.some_func = some_func
        functools.update_wrapper(self, some_func)

    def __call__(self, *args, **kwargs):
        return self.some_func(*args, **kwargs)


@outer
def add(x, y):
    """adds a x and y"""
    return x + y

if __name__ == '__main__':
    print add.__name__


