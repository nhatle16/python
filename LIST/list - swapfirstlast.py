n = int(input("Enter the length: "))
myList = []

for i in range(0,n):
    el = input("Enter element: ")
    myList.append(el)

def swapList(newList):
    size = len(newList)
    if size >= 2:
        temp = newList[0]
        newList[0] = newList[size-1]
        newList[size-1] = temp
    return newList

print(swapList(myList))