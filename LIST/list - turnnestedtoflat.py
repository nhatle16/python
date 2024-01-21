# Nested list is a list with in a list

lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

# 1: Using for loops

def flat(lis):
    flatList = []
    
    for element in lis:
        if type(element) is list:
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

print(flat(lis))

# 2: Using list comprehension

flatList = [item for innerList in lis for item in innerList]

print(flatList)

# 3: Using recursion

res = []

def removeNested(lis):
    for i in lis:
        if type(i) == list:
            removeNested(i)
        else:
            res.append(i)

removeNested(lis)

print(res)