"""
filter: Construct an iterator from those elements of iterable for which function returns true
"""
def filter_x(x):
    if x:
        return x+1

print(filter(filter_x, []))
print(filter(filter_x, [1,2,3, '', None]))
print(filter(None, [1,2,3, '', None]))

"""
map: Return an iterator that applies function to every item of iterable, yielding the results
"""

def map_x(x):
    return x+1
print(map(map_x, [1,2,3]))


def map_xy(x, y):
    if x and y:
        return x + y
    else:
        return "iterable-exhausted"
print(map(map_xy, [1,2,3], [11, 22, 33]))
print(map(map_xy, [1,2,3], [11, 22, 33, 44]))
print(map(map_xy, [1,2,3, 4, 5], [11, 22, 33, 44]))


"""
next: Retrieve the next item from the iterator
"""
iterator = iter([1,2,3])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator, 'default'))
print(next(iterator, 'default')) # not printed



"""
super
"""

class BaseTest:
    def test_setup(self):
        print("BaseTest: test_setup")
        super(BaseTest, self).test_setup()

class APITest:
    def test_setup(self):
        print("APITest: test_setup")

class UnitTest(BaseTest, APITest):
    def test_setup(self):
        print("UnitTest: test_setup")
        super().test_setup()

unit_test = UnitTest()
unit_test.test_setup()
print("*****")
super(UnitTest, unit_test).test_setup()


"""
isinstance and issubclass
"""
class Movie(object):
    pass

obj = Movie()

print("*** isinstace ***")
print(isinstance(unit_test, UnitTest))
print(unit_test.__class__ is UnitTest)
print(isinstance(unit_test, (UnitTest, APITest, BaseTest)))

""" type testing"""
print("type ..... ")
print(isinstance(UnitTest, type))
print(isinstance(Movie, type))
print(isinstance(unit_test, type))  # False
print(isinstance(obj, type))  # False
""" obj testing """
print("object .....")
print(isinstance(UnitTest, object))
print(isinstance(Movie, object))
print(isinstance(unit_test, object))
print(isinstance(obj, object))
print("type and object ......")
print(isinstance(type, object))
print(isinstance(object, type))




print("*** issubclass ***")
print(issubclass(UnitTest, UnitTest))
print(issubclass(UnitTest, (UnitTest, APITest, BaseTest)))
print(issubclass(UnitTest, type))
print(issubclass(UnitTest, object))
