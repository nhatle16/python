# BINARY SEARCH
# Binary Search  =  search algorithm that finds the position of the value within the sorted list
#                   half of the list is remove after each step
# Complexity : O(log(n))

import random as rand

def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = int((left + right) / 2)
        print(arr[mid])
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
            
    return -1

def main():
    arr = [12, 17, 20, 25, 25, 30, 42, 42, 42, 50, 50, 63, 75, 80, 87, 99]
    value = 75
    res = binary_search(arr, value)

    if res == -1:
        print('Not found')
    else:
        print(f'The value {value} is found at index: {res}')

main()

