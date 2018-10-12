a = [1, 2]
b = [2, 3, 4]

c = a + b

for cc in c:
    print(cc)

data = {'birthyear_from': '0', 'birthyear_to': '0',
        'height': '0', 'education': '0'}

if all([_ in data for _ in ('birthyear_from', 'birthyear_to', 'height', 'education')]):
    print('yes')
else:
    print('no')

print(data.values())
if any([d != '0' for d in data.values()]):
    print('yes')
else:
    print('no')

print([_ in data for _ in ('birthyear_from', 'birthyear_to', 'height', 'education')])
