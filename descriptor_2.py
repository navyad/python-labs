class Person(object):
    def __init__(self):
        self._name = ''

    def fget(self):
        print "Getting: %s" % self._name
        return self._name

    def fset(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    def fdel(self):
        print "Deleting: %s" %self._name
        del self._name

    name = property(fget, fset, fdel, "I'm the property.")


person = Person()
person.name = "navyad"
person.name
del person.name
#person.name



class Cricket:
    def __init__(self):
        self._team = "India"

    @property
    def team(self):
        return self._team


obj = Cricket()
print obj.team
print "ccc", obj._team
obj.team = "England"
print obj.team
# following will not work
obj._team = "Aus"
print obj.team
