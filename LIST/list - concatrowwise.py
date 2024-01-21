lis1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
lis2 = [[1, 3], [9, 3, 5, 7], [8]]

for idx, value in enumerate(lis1):
    new_values = []
    for j in lis2[idx]:
        new_values.append(j)
    lis1[idx].extend(new_values)

print(lis1)
