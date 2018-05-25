from simplejson import encoder, JSONEncoder

py_list = [1, 4, 6, 2, 8, 7]
py_dict = {"z": 12, "k": 5, "c": 23}
py_tuple = (33, 55, 11)

# Encoding
# 1: circular rerefeces
name = ["nav" , "yad"]
name[0] = name
encoder_1 = JSONEncoder()
#print(encoder_1.encode(name)    # ValueError: Circular reference detected

# 2: dict key sorted
encoder_1 = JSONEncoder(sort_keys=True)
res = encoder_1.encode(py_dict)
print(res)


# 3: default
def serialize_this(arg):
    return "aaa"

class ABC:
    pass

obj = ABC()
encoder_1 = JSONEncoder(default=serialize_this)
res = encoder_1.encode(obj)   # this obj is passed to serialize_this()
print(res)
