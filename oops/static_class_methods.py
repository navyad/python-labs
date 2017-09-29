class Marks(object):

    @staticmethod
    def static_foo(score):
        if score == 100:
            return 'A'
        elif score == 60:
            return 'B'
        else:
            return 'C'

    @classmethod
    def class_bar(cls, grade):
        if grade == 'A':
            return 100
        elif grade == 'B':
            return 60
        else:
            return 30

obj = Marks()
print(obj.static_foo(100))
print(Marks.static_foo(40))

print(obj.class_bar('A'))
print(Marks.class_bar('C'))


class Math(object):

    def add(x, y):
        return x + y

    def sub(cls, x, y):
        return x - y

Math.add = staticmethod(Math.add)
print(Math.add(12, 10))

Math.sub = classmethod(Math.sub)
print(Math.sub(12, 10))



# http://www.geeksforgeeks.org/class-method-vs-static-method-python/
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
     
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))