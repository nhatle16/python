lis1 = [1,3,5,7,9]
lis2 = [0,2,4,6,8]

# 1: Using "+" operator
res1 = lis1.copy()
res1 = res1 + lis2

print(res1)

# 2: Using list comprehension:
res2 = [y for x in [lis1,lis2] for y in x]

print(res2)

# 3: Using method extend()
res3 = lis1.copy()
res3.extend(lis2)

print(res3)

# 4: Using "*" operator
res4 = [*lis1, *lis2]

print(res4)

