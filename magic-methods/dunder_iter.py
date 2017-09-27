class NumIter:
    """
    implementing iterator protocol using __iter__
    this iterator returns next three numbers
    """
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        print "__iter__"
        self.count = 0
        return self

    def next(self):
        print "__next__"
        if self.count == 3:
            raise StopIteration()
        else:
            self.count += 1
            return self.num + self.count


obj = NumIter(10)
for num in obj:
    print num
print '*'*80

"""
iter takes an iterable
"""
iter_obj = iter(obj)
print next(iter_obj)
print next(iter_obj)
print next(iter_obj)
try:
    next(iter_obj)
except StopIteration:
    print "StopIteration occured"
print '*'*80

"""
iter takes callable
"""
class DefaultNum:
    count = 0

    def get_num(self):
        self.count += 1
        return self.count

obj = DefaultNum()
for x in iter(obj.get_num, 15):
    print x
