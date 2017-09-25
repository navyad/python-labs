
class Cinema(object):

    movie_name = "avatar"
    director = "james"

    def __getattr__(self, name):
        """
        called when obj.attr supposed to throw AttributeError
        this method should either return some value or raise AttributeError
        """
        print "getattr: {0}".format(name)
        return 'some-value'

    def __getattribute__(self, name):
        val = object.__getattribute__(self, name)
        print "getattribute: {0}".format(name)
        return val

    def __setattr__(self, name, value):
        print 'set %s to %s' % (name, repr(value))
        object.__setattr__(self, name, value)


cin_2 = Cinema()
cin_2.movie_name = "seven"
print cin_2.movie_name
setattr(cin_2, 'director', 'david-fincher')
print cin_2.director
print cin_2.poi
print '*'*100


class Ticket(object):
    def __new__(cls, *args, **kwargs):
        print "new called: {}".format(cls)
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        print "init called"

    def __call__(self):
        print "call called"


print "-"*80
obj = Ticket()
print obj.attr1
obj()
