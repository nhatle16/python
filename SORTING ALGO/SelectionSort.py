# SELECTION SORT  
  
# Array is considered into 2 parts: unsorted and sorted
#   1. Select the lowest element in the remaining array
#   2. Bring it to starting position
#   3. Change the counter of unsorted array by 1

# Complexity: O(n^2)

import random as rand

def selection_sort(arr):
    # Traverse through all elements
    for i in range(len(arr)):
        
        # Find min element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            # Loop until the smallest is found
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum with 
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    array = [64, 25, 12, 22, 11]

    selection_sort(array)

    print("Sorted array using selection sort:")
    for x in array:
        print(x, end=' ')

main()