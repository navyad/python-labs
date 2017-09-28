"""
https://docs.google.com/document/d/153FBwDfmBM8d4n8uNWzactaVZy-8000gRmvZUwGMmVA
"""


print "str test"
my_name = "nav"
your_name = "nav"
print my_name == your_name      #True
print hash(my_name) == hash(your_name) #True
print my_name is your_name      #True
print id(my_name) == id(your_name) #True


print "tuple test"
my_tup = ("nav",)
your_tup = ("nav",)
print my_tup == your_tup   #True
print hash(my_tup) == hash(your_tup)   #True
print my_tup is your_tup   #False
print id(my_tup) == id(your_tup)  #False


# update my_name
print id(my_name)
my_name += "yad"
print id(my_name)

print  "\ntwo equal objects has to have same hash value"
city = "delhi"
capital = "delhi"
print hash(city) == hash(capital)
print city.__hash__() == capital.__hash__()


print  "\nall hashable can be used as a key"
print {"a": "a"}
print {1: "1"}
print {1.9: "1.9"}
print {(1,): "tup-val"}


print  "\ncreate immutable object"
from collections import namedtuple
Point = namedtuple('Point',['x', 'y'])
p1 = Point(x=9, y=10)
try:
    p1.x = 12
except AttributeError as exp:
    print "AttributeError: {0}".format(exp.message)



print "\npassing immutable to function"
def update_arg(name_tup):
    name_tup += ("yadav",)
    print "in function: ", name_tup

name_tup = ("naveen",)
print "before passing: ", name_tup
print update_arg(name_tup)
print "after passing", name_tup


print "\nchange value of immutable ref in function"
def assign_value(ref, new_val):
    ref = new_val
    print("Inside:", ref)

immutable_data = "old value"
print("Before:", immutable_data)
assign_value(immutable_data, "new value")
print("After:", immutable_data)
