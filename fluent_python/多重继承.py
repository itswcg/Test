class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)


class C(A):
    def pong(self):
        print('PONG', self)


class D(B, C): # 先继承B，C, 用D.__mro__查看顺序

    def ping(self):
        super().ping()
        print('pong-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

a = A()
b = B()
c = C()
d = D()

print(a.ping())
print(c.ping())
print(d.pong())
print(C.pong(d))
print(D.__mro__)
print(d.ping())
print(d.pingpong())

