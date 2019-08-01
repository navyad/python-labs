def double_num(num):
    while True:
        num *= 2
        yield num



gen_obj = double_num(12)
print "using next..."
print gen_obj.send(None)
print gen_obj.next()
print gen_obj.next()
print gen_obj.next()
print gen_obj.next()

gen_obj_2 = double_num(3)
print "using send..."
print gen_obj_2.send(None)
print gen_obj_2.send(1)
print gen_obj_2.send(4)
