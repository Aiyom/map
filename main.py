from inspect import ismethod


class Map(dict):

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict) and hasattr(arg, 'iteritems') and ismethod(getattr(arg, 'iteritems')):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs and hasattr(kwargs, 'iteritems') and ismethod(getattr(kwargs, 'iteritems')):
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


m = Map({'name': 'Dict with dot'}, year=2023, hobby=['dance', 'sleep'])

m.name = 'Bobo'
print(m)