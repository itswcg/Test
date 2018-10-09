# 元编程是动态创建属性


# 把一个Json数据集转换为嵌套的FrozenJson对象
from collections import abc


class FrozenJSON:

    def __new__(cls, arg):
        pass  # 用new代替build

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():  # 避免python关键字
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
