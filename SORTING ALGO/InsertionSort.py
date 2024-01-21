# INSERTION SORT

# Iterate through an array and compare the current element (key) 
# to its predecessors, if the key is smaller than the predecessor
# compare it to the elements before. Move the greater elements 1 
# position up to make space for the swapped element

#
import numpy as np

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] >= key:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key      
        
lis = [9,5,3,6,7,1,2]
array = np.array(lis)

insertion_sort(lis)
insertion_sort(array)

print(lis)
print(array)