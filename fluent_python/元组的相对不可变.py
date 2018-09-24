t1 = (1, 2, [30, 40])
t2 = t1
print(t1==t2, t1 is t2)

# 循环引用
a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
[10, 20, [[...], 30]]

# 不要使用可变类型作为参数的默认值

class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
