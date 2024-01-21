list = [10, 30, 20, 60, [90, 40, 70]]

# Printing sublist at index 4
print(list[4])

# Printing 1st element of the sublist
print(list[4][0])

# Printing 2nd element of the sublist
print(list[4][1])

# Printing 3rd element of the sublist
print(list[4][2])

# --------------------------------------------------------------------------

name_list = [["A", 20], ["B", 20]]

for name in name_list:
    print(name[0], "is", name[1], "years old")

for name, age in name_list:
    print(name,"is",age,"years old")

# --------------------------------------------------------------------------

new_list = [10, 20, 30, 40, [70, 90, 60]]

print(new_list[4])
print(new_list[4][:])
print(new_list[4][0:3])

