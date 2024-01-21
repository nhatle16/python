lis = [4, 5, 7, 3, 9, 14, 16, 30, 11, 26, 12, 10]

value = int(input("Enter a value need to remove: "))

# 1: Using method pop()

def remove1(mylis, value):
    for i in mylis:
        if i == value:
            mylis.pop(mylis.index(value))
    return mylis

print(remove1(lis.copy(), value))

# 2: Using method remove()
def remove2(mylis, value):
    mylis.remove(value)
    return mylis

print(remove2(lis.copy(),value))

