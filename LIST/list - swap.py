n = int(input("Enter the length: "))

my_list = []

for i in range(n):
    el = int(input("Enter an element: "))
    my_list.append(el)

def swapIndex(newlist):
    size = len(newlist)

    pos1 = int(input("Enter 1st position: "))
    pos2 = int(input("Enter 2nd position: "))

    while pos1 >= size:
        pos1 = int(input("Enter 1st position: "))

    while pos2 >= size:
        pos2 = int(input("Enter 2nd position: "))

    temp = newlist[pos1]
    newlist[pos1] = newlist[pos2]
    newlist[pos2] = temp
    return newlist

print(swapIndex(my_list))

    

