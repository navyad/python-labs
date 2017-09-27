class Movie:

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, name):
        self.data[key] = name

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

obj = Movie()
obj['name'] = 'fightclub'
obj['director'] = 'david fincher'

print obj['name']
print obj['director']
print "keys", obj.keys()
print "values", obj.values()

del obj['name']

try:
    obj['name']
except KeyError as exp:
    print "KeyError: {}".format(exp.message)
