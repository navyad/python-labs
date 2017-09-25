"""
repr: offical representaion of object
str: informal represendtation of object
"""

class Movie(object):

    """
    if a class defines __repr__ not __str__
    then __repr__ is called for both repr() and str()
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print "calling repr ..."
        return 'Movie({})'.format(self.name)

obj = Movie('seven')

# both calls __repr__()
repr(obj)
str(obj)



class Director(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        print "calling str....."
        return 'Director({})'.format(self.name)


print "*"*80
obj = Director('david')

# calls default repr
repr(obj)
# calls defined str
str(obj)



class MovieDirector(object):

    def __init__(self, movie_name, director_name):
        self.movie_name = movie_name
        self.director_name = director_name

    def __repr__(self):
        print "MovieDirector repr....."
        _repr_str = "<%s: %s>" % (self.__class__.__name__, self or "None")
        return _repr_str


    def __str__(self):
        """
        if commented:
        RuntimeError: maximum recursion depth exceeded while getting the str of an object
        """
        print "MovieDirector  str....."
        return self.movie_name+"-"+self.director_name


print "*"*80
obj = MovieDirector('seven', 'david')
repr(obj)
str(obj)



print "*"*80
# how to implement repr and str, see the diffrence below
from datetime import datetime
now = datetime.now()
print repr(now)
print str(now)
