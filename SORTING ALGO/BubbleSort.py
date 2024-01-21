# BUBBLE SORT

# Repeatedly swapping the adjacent elements if they are in wrong order
#   1. Traverse from the left and compare with adjacent value
#   2. Placed the highest one on the right side --> the largest is moved to the rightmost
#   3. Continue with the remained unsorted array

# Not suitable for large data
# Complexity: O(n^2)
# No. of passes:  n-1
# No. of comparisons: n*(n-1)/2

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n):
        swapped = False
        # Exclude i elements since they are already in placed
        # Traverse from 0 to n-i-1
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next one
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False: # The array is sorted already  
            break

def main():
    array = [64, 25, 12, 22, 11]

    # Performing bubble sort
    bubble_sort(array)

    print('Sorted array using bubble sort: ')
    for x in array:
        print(x, end=' ')

main()
