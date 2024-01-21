# QUICK SORT

# Base on Divide and Conquer algorithm

#   1. Pick up a pivot (last element) and partition the array around the pivot by placing the pivot in its correct position
#   2. Recursively consider the left part and right part

# Complexity: O(nlog(n))

# Find the partition position 
def partition(arr, l, h):
    # Create pivot as the rightmost element
    pivot = arr[h]

    # Index of greater element
    i = l - 1
    
    # Traverse all elements and compare it with pivot
    for j in range(l, h):
        if arr[j] <= pivot:
            # Increase the index of greater element by 1    
            i += 1
            # If element smaller than the pivot is found
            # Swap it with the greater element pointed by i
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot with the greater element indexed by i
    arr[i+1], arr[h] = arr[h], arr[i+1] 
    # Return the pivot position
    print(arr)
    return i+1

def quick_sort(arr, l, h):
    if l < h:
        # Find pivot such that
        # Smaller elements are on the left
        # Greater elements are on the right
        pi = partition(arr, l, h)
        # Recursive call on the left of pivot   
        quick_sort(arr, l, pi-1)
        
        # Recursive call on the right of pivot
        quick_sort(arr, pi+1, h)
        

def main():
    array = [25, 63, 25, 30, 87, 75, 50, 17, 42, 42, 20, 99, 80, 12, 50, 42]
    length = len(array)
 
    # Function call
    quick_sort(array, 0, length - 1)
    # print('Sorted array using quick sort:')
    # print(array)
    # for x in array:
    #     print(x, end=" ")

main()