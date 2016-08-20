import abc


class DoubleBaseModel(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def value(self):
        return "<oo>"

    @property
    @abc.abstractmethod
    def constant(self):
        return "<oo>"


# Concrete implementations
class DjangoModel(DoubleBaseModel):

    value = "django value"

    def constant(self):
        return "django constant"
  

if __name__ == '__main__':
    django = DjangoModel()
    print(django.value)
    print(django.constant())
