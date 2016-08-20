import abc


class DoubleBaseModel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_dict(self, num):
        self._id = num
        return {"id": self._id}


# Concrete implementations
class DjangoModel(DoubleBaseModel):

    def to_dict(self, _id):
        _super_obj = super(DjangoModel, self)
        return _super_obj.to_dict(_id)


if __name__ == '__main__':
    django = DjangoModel()
    print(django.to_dict(123))
