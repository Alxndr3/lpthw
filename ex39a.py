things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

stuff = {'name': 'Zed', 'age': 39, 'heigh': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['heigh'])

stuff['city'] = "SF"
print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff)
print(stuff[1])
print(stuff[2])

for x in stuff.items():
    print(x)

for x in stuff.values():
    print(x)

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
