def outer(some_func):
    def inner(a, b):
        if a > b :
            fr = some_func(a, b)
        else:
            fr = -1
        return fr
    return inner


@outer
def add(x, y):
    return x + y

@outer
def sub(x, y):
    return x - y

if __name__ == '__main__':
    print add(9, 2)
    print add(2, 2)

    print sub(9, 2)
    print sub(0, 0)


