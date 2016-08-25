def outer(some_func):
    def inner(a, b):
        return some_func(a, b)
    return inner


@outer
def add(x, y):
    """adds a x and y"""
    return x + y

if __name__ == '__main__':
    print add.__name__ # inner
