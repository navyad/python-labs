class A:
    def _poi_(self):
        return "a: poi"

    def __pro(self):
        return "a: pro"

class B(A):
    def _poi_(self):
        return "b: poi"




a = A()
print dir(a) # ['_A__pro', '__doc__', '__module__', '_poi_']
print a._poi_()
try:
    print a.__pro()
except AttributeError as exp:
    print exp.message

print a._A__pro()

b = B()
print dir(b)
print b._poi_()
print a._A__pro()

