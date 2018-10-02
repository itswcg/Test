# any和all 会短路,即一旦确定了结果就立即停止使用迭代器

print(bool(0.0))
print(all([1, 2, 3]))
print(all([1, 0, 3]))
print(any([1, 0, 2]))
print(any([0, 0, 0.0]))

# iter
from random import randint


def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print(d6_iter)

for roll in d6_iter:
    print(roll)

with open('test.txt') as fp:
    for line in iter(fp.readline, '\n'):
        process_line(line)
