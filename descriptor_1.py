class NoneNegative(object):
    def __init__(self, default):
        self.val = default

    def __get__(self, obj, obj_type):
        print "get:"
        return self.val

    def __set__(self, obj, val):
        if val < 0:
            raise ValueError("Negative not allowed")
        self.val = val
        print "set to {0}".format(val)


class Movie(object):
    name = "Seven"
    rating = NoneNegative(0)

movie = Movie()
print movie.name

print movie.rating
movie.rating = 9
print movie.rating


movie.rating = -1
