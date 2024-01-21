import random as rand

dict = {}

x = rand.randint(0, 10)
y = rand.randint(0, 10)
z = rand.randint(0,10)

dict[x, y, z] = x - y + z

x, y, z = 1, 6, 6

dict[x, y, z] = x + y - z

print(dict)