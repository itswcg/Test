# 除非编写框架,否则不要用元类


def recore_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attts.update(kwargs)
        for name, value in atrrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i)
                           for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    return type(cls_name, (object,), cls_attrs)


Dog = recore_factory('Dog', 'name weight owner')

1, 11, 2, 3, 5, 12, 7, 8, 13, 9, 10, 14

import evaltime
100, 400, 700, 1, 2, 6, 7, 200, 9, 14

# 所有顶层代码在导入模块时运行, 解释器会编译, 但不会执行定义体

python3 evaltime.py
100, 400, 700, 1, 2, 6, 7, 200, 9, 11, 3, 5, 12, 300, 13, 10, 14, 4

object是type的实例, type是object的子类
所有类都是type的实例, 但元类还是type的子类
