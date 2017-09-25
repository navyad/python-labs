"""
Python has always provided a variety of built-in and standard-library generic functions,
such as len() , iter() , pprint.pprint() , copy.copy() , and most of the functions in the operator module.
However, it currently:
    does not have a simple or straightforward way for developers to create new generic functions,
    does not have a standard way for methods to be added to existing generic functions
In addition, it is currently a common anti-pattern for Python code to inspect the types of received arguments,
in order to decide what to do with the objects.

For example, code may wish to accept either an object of some type, or a sequence of objects of that type.
Currently, the "obvious way" to do this is by type inspection, but this is brittle and closed to extension.
"""


from functools import singledispatch

# ................... generic function
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("verbosing....")
    print(arg)

# ................... overloaded functions
@fun.register(int)
def fun_int(arg, verbose=False):
    if verbose:
        print("numbers: ")
    print(arg)

@fun.register(list)
def fun_list(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    print([ele+1 for ele in arg])

@fun.register(object)
def fun_int(arg):
    print(arg.__class__)


if __name__ == '__main__':
    fun("function overloading in python")
    fun(23, True)
    fun([11, 22, 33])
    fun(object())
