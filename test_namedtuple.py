_class_template = """\
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class {typename}(tuple):
    '{typename}({arg_list})'

    __slots__ = ()

    _fields = {field_names!r}

    def __new__(_cls, {arg_list}):
        'Create new instance of {typename}({arg_list})'
        return _tuple.__new__(_cls, ({arg_list}))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new {typename} object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != {num_fields:d}:
            raise TypeError('Expected {num_fields:d} arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new {typename} object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, {field_names!r}, _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '({repr_fmt})' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

{field_defs}
"""

_repr_template = '{name}=%r'

_field_template = '''\
    {name} = _property(_itemgetter({index:d}), doc='Alias for field number {index:d}')
'''



def get_definition(typename, field_names):
    return _class_template.format(
            typename = typename,
            field_names = tuple(field_names),
            num_fields = len(field_names),
            arg_list = repr(tuple(field_names)).replace("'", "")[1:-1],
            repr_fmt = ', '.join(_repr_template.format(name=name)
                                 for name in field_names),
            field_defs = '\n'.join(_field_template.format(index=index, name=name)
                                   for index, name in enumerate(field_names))
        )


name_type = 'point'
class_def = get_definition(name_type, ['x', 'y', 'z'])
print(class_def)

namespace = dict(__name__='namedtuple_%s' % name_type)
print(namespace)
exec(class_def, namespace)
result = namespace[name_type]
print(result)
