import pickle as p

class Vector:
    pass

class Group:
    pass

x = Vector()
x.data = [Group(), Group()]
x.data[0].y = 90
x.data[0].k = 44
x.data[1].y = 3456
x.data[1].k = 8583


# dump information to that file
j = p.dumps(x)

print(j)

d = p.loads(j)

print(d.data[0].y)
print(d.data[0].k)
print(d.data[1].y)
print(d.data[1].k)
