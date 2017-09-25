"""
examples: del or __delattr__
"""


class Movie:
    name = ""

    def __init__(self, name):
        self.name = name


"""
del: Deletion of a name removes the binding of that name from the local or global namespace
"""
movie = Movie('7')
print 'movie' in globals(), 'movie' in locals()
print "deleting movie"
del movie
print 'movie' in globals(), 'movie' in locals()


class FavMovie(object):
    name = ""

    def __init__(self, name):
        self.name = name

    def __delattr__(self, name):
        print name, "deleting attribute"
        object.__delattr__(self, name)

    def __del__(self):
        print "del"

print '*'*100
fav_movie = FavMovie('fighclub')
print fav_movie.name
del fav_movie.name
print fav_movie.name
del fav_movie
try:
    fav_movie
except NameError as exp:
    print exp.message

new_fav = FavMovie('seven')
new_fav.__del__()
print new_fav


class MovieList(object):
    """
    exception comes del is called
    """
    def __init__(self, x):
        if x == 0:
            raise Exception()
        self.x = x

    def __del__(self):
        print "del", self.x

MovieList(0)
