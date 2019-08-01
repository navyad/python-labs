from contextlib import contextmanager


@contextmanager
def mul(items):
    print "enter: "
    for x in map(lambda x : x * 3, items):
        yield x
    print "end"



inps = [1,2,3]
print (y for y in mul(inps))
