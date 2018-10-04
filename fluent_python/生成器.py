print(list(range(9)))

# 可迭代对象实现 __iter__方法
# 迭代器 __iter__ 和 __next__ 方法


def triangles():
    L = [1]
    n = 0
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(n) if n + 1 <= n] + [1]
        n = n + 1
