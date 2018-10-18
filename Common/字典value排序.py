import json, re
h1 = '''{
    "100人以下": "99",
    "100-300人": "199",
    "300-1000人": "299",
    "1000人以上": "599"
}
'''
print(h1)
jsonUser = json.loads(h1)
print(jsonUser.keys())

# for i in jsonUser.keys():
#     print(i.split('人')[0])

# a = "100人以下"
# print(a.split('人')[0])
a = 88
user = list(jsonUser.keys())
b1 = user[0].split('人')[0]
b2 = user[1].split('人')[0].split('-')[1]
b3 = user[2].split('人')[0].split('-')[1]

print(user[0])
if a < int(b1):
    print(jsonUser[user[0]])


print(sorted(jsonUser.items(), key=lambda d: int(d[1])))
prices = sorted(jsonUser.items(), key=lambda d: int(d[1]))
print(prices[0][0])

s = re.findall("\d+", prices[2][0])[1]
print(s)
