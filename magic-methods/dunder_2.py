from collections import Counter


"""
examples for __eq__() and __hash__()
"""


class Movie:
    """
    if it defines __eq__() but not __hash__(),
    its instances will not be usable as items in hashable collections
    """
    name = ""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


print "*"*100
n = Movie('fightclub')
p = Movie('fightclub')

# equality test
print n == p
print n is p

# since hash is not defined, objects are not hashable
try:
    Counter([n, p])
except TypeError as exp:
    print exp.message


class FavMovie:
    """
    make class hashbale
    """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        "calling __eq__"
        return self.name == other.name

    def __hash__(self):
        return hash((self.name))


print "*"*100
fav = FavMovie('fighclub')
fav_counter = Counter([fav])
print fav_counter


class Cinema(object):
    """
    class defined from object has buit in __eq__ and __hash__
    """
    movie_name = ""
    director = ""

    def __init__(self, movie_name, director):
        self.movie_name = movie_name
        self.director = director


print "*"*100
cinema = Cinema('fightclub', 'david fincher')
cinema_2 = Cinema('seven', 'david fincher')
cinema_3 = Cinema('seven', 'david fincher')

# equals check
print cinema_2 == cinema_3

# hashable
counter = Counter([cinema, cinema_2])
print counter.items()
