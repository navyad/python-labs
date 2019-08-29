class Singleton (object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'self'):
            cls.self = object.__new__(cls)
        return cls.self
#Usage
mySingleton1 = Singleton()
mySingleton2 = Singleton()

#mySingleton1 and  mySingleton2 are the same instance.
assert mySingleton1 is mySingleton2
