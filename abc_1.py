import abc


class BaseModel(metaclass=abc.ABCMeta):

    def to_dict(self, _id):
        self._id = _id
        return {"id": self._id}


class DoubleBaseModel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_dict(self, _id):
        return {"id": self._id}


# Concrete implementations
class DjangoModel(DoubleBaseModel):
    pass


class FlaskModel(DoubleBaseModel):

    def to_dict(self):
        return "boom boom"


if __name__ == '__main__':
    base = BaseModel()
    print(base.to_dict(123))

    try:
        DoubleBaseModel()
    except TypeError as err:
        print(err)

    try:
        DjangoModel()
    except TypeError as err:
        print(err)

    flask = FlaskModel()
    print(flask.to_dict())
