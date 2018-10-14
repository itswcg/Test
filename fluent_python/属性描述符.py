# 理解属性描述符是精通Python的关键
# 描述符的用法, 创建一个实例, 作为另一个类的类属性
# Django model 是描述符
# 如果要对类属性有要求, 就可以用理解描述符

# 超类 内置如__init__ __get__要用super, 普通方法可以不用


class Quantity:  # 描述符类 , 可以重用, 易扩展

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):  # instance 描述符实例
        if value > 0:
            instance.__dict__[self.storage_name] = value  # 托管__dict__属性
        else:
            raise ValueError('value must be > 0')


class Quantity:  # 特性工厂, 简单
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storange_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    retun property(qty_getter, qty_setter)


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, descprition, weight, price):
        self.descprition = descprition
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
