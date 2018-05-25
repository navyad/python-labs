"""
Immutables data types:
    int, float, long, complex
    str
    bytes
    tuple
    frozen set
"""


# test1
name = "python"
def test_str(_str):
    return _str + "-rocks"
print name  # python
print test_str(name) # python-rocks
print name # python
print "......"

# test 2
my_country = "India " # a string object created with "India" refercen is assiged to my_country variable
your_country = my_country
your_country += "France"
print my_country # India
print your_country # India France
print "......"

# test 3
my_country = "U.S"
# another string object created at this point two string objects are present "India" and "U.S", this time my_country refers to "U.S"
print my_country

# test 3: immutables cannot be changed in place
print my_country[0]
try:
    my_country[0] = "K"
except TypeError as exp:
    # 'str' object does not support item assignment
    print exp.message


"""
Mutables data types:
    list, dict, set
"""

my_list = [1,2,3]
your_list = ["a", "b", "c"]
your_country = my_list
your_country.append("foo")
print my_list # [1, 2, 3, 'foo']
print your_country # [1, 2, 3, 'foo']



other_list = [11, 22, 33]
def test_list(_list):
    _list.append("bar")
test_list(other_list)
print other_list # [11, 22, 33, 'bar']

# mutables can be changed in place
other_list[3] = "foo-bar"
print other_list
