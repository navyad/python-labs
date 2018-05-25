from itertools import chain, groupby
from operator import itemgetter



"""
groupby
"""
# unique items from string
_res = [k for k, g in groupby('AAAABBBCCDEEEEF')]
print(_res) #

# group consecutive occurrences
_res = [list(g) for k, g in groupby('AAAABBBCCD')]
print(_res)

# group certain items
movies = [ ("thriller", "seven"), ("drama", "boyhood"), ("comedy", "analyze this"),  ("drama", "titanic"), ("thriller", "fight club")]
sorted_movies = sorted(movies, key=lambda x: x[0])
for key, item in groupby(sorted_movies, key=itemgetter(0)):
        list_of_movies = ", ".join([thing[1] for thing in item])
        _res = "{0}: {1}".format(key, list_of_movies)
        print(_res)
