import itertools, time

sample = [1, 2, 3]
print(list(itertools.accumulate(sample)))

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']

print(list(zip(L1, L2)))

print(list(itertools.chain(L1, L2)))
