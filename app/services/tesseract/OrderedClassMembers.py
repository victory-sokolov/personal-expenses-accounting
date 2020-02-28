import collections


class OrderedClassMembers(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()

    def __new__(cls, name, bases, classdict):
        classdict['__ordered__'] = [key for key in classdict.keys()
                                    if key not in ('__module__', '__qualname__')
                                    and not key.startswith("__")
                                    ]
        return type.__new__(cls, name, bases, classdict)
