# JUMP SEARCH
# Jump Search = search algorithm that finds the position of a value in a sorted list
#               check fewer elements by jump ahead by fixed steps 
# Complexity: O(sqrt(n))
# List of size n and block (to be jump) size m
# Worst case: n/m jumps + linear search for m-1 elements
# No. of comparison: n/m + m - 1
# Minimum value of m: m = sqrt(n)

import math 
import random as rand
from datetime import datetime

def jump_search(arr, key):
    l = len(arr)
    step = math.floor(math.sqrt(l))

    # Finding for the block that  
    # the value is present
    prev = 0
    while arr[min(step, l)-1] < key:
        prev = step
        # Jump to next block
        step += math.floor(math.sqrt(l))
        if prev >= l:
            return -1
    
    while arr[prev] < key:
        prev += 1
        # If we reached next block or end 
        # of list, element is not present.
        if prev == min(step, l):
            return -1

    # If element is found    
    if arr[prev] == key:
        return prev
    return -1

def main():
    lis = list(range(1,100001))
    key = rand.randint(1,100001)
    print(key)
    index = jump_search(lis, key)
    print(index)
        
main()
