class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


class Foo:
    pass

if __name__ == '__main__':
    vector_1 = Vector(5, 2)
    vector_2 = Vector(3, 2)
    vector_3 = vector_1 + vector_2
    # __repr__ would print Vector(5, 2)
    print(vector_3)

    # (4 * vector_2) not possible
    print(vector_2 * 4)

    # user deinfed classes are truthy
    # unless __bool__ or __len__ is implemented
    print(bool(Foo()))

    vector_4 = Vector(0, 0)
    print(bool(vector_4))
