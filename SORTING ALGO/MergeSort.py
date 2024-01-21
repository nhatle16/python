# MERGE SORT

# Base on Divide and Conquer algorithm

# Divide list into sublists until there is only one element each sublist
# Compare a list made of pair of sublists and then merge the sorted sublists
# Recursively perform until final list is formed

# Complexity: O(nlog(n))

def merge_sort(arr):
    # Condition to execute the function
    # Stop if there is only 1 element in array
    if len(arr) > 1:
        mid = len(arr) // 2

        # Define the left half 
        L = arr[:mid]
        # Define the right half
        R = arr[mid:]

        # Sort on left side
        merge_sort(L)
        # Sort on right side
        merge_sort(R)

        # Initiate indexes
        i, j, k = 0, 0, 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                # Move to next element in L to compare
                i += 1
            else: 
                arr[k] = R[j]
                # Move to next element in R to compare
                j += 1
            # Move to next element of the main array
            k += 1

        # Check if there were elements left
        # On the left side
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1 
        # On the right side
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

def main():
    arr = [64, 25, 12, 22, 11]

    merge_sort(arr)

    print('Sorted array using merge sort: ')
    for x in arr:
        print(x, end=' ')

main()