from array import *

arr = array('i', [2,5,3,6,2,1,4,5])
arr1 = array('i', [1,2,3,4])

def find_duplicate(arr):
    num_set = set()
    no_duplicate = -1
    
    for i in range(len(arr)):
        if arr[i] in num_set:
            return arr[i]
        else:
            num_set.add(arr[i])
    
    return no_duplicate

print(find_duplicate(arr))
print(find_duplicate(arr1))