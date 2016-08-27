class Person(object):

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print "Getting: %s" % self._name
        return self._name

    @name.setter
    def name(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    @name.deleter
    def name(self):
        print ">Deleting: %s" % self._name
        del self._name

person = Person()
person.name = "navyad"
person.name
del person.name
person.name
