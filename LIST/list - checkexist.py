my_list = [1,6,8,3,2,6,2,0]

n = int(input("Enter a value: "))
exist = False
for i in my_list:
    if i == n:
        exist = True

print(exist)
    