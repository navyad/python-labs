# ........................ mutable types: behave as pass by value
def swap(list_1, list_2):
    list_3 = list_2
    list_2 = list_1
    list_1 = list_3
    print "Inside: function", list_1, list_2


list_1 = [1, 11, 111]
list_2 = [2, 22, 222]
print list_1, list_2
swap(list_1, list_2)
print list_1, list_2


# ........................ mutable types: behave as pass by ref

def update_list(my_list):
    my_list.append(4)


my_list = [1, 2, 3]
print my_list
update_list(my_list)
print my_list

