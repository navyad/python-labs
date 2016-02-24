def outer(some_func):
    def inner(a, b):
        if a > b :
            fr = some_func(a, b)
        else:
            fr = -1
        return fr
    return inner


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

if __name__ == '__main__':
    func_inner_add = outer(add)
    print func_inner_add(9, 2)
    print func_inner_add(2, 2)

    func_inner_sub = outer(sub)
    print func_inner_sub(9, 2)
    print func_inner_sub(0, 0)

