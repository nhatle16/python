lis1 = ["gfg","is","best"]
lis2 = ['for','CS']    

# 1: Use list comprehension
temp1 = [(a, b) for a in lis1 for b in lis2]

res1 = [x + ' ' + y for (x, y) in temp1]

print(res1)

# 2: Using for loop
res2 = []

for i in lis1:
    for j in lis2:
        value = i + ' ' + j
        res2.append(value)

print(res2)