# Find the common values between 2 arrays

import numpy as np

# intersection(): return a set of intersections between 2 arrays
# np.intersect1d(): return a sorted, unique array of values that are in both arrays

# Using list comprehension
def findCommon(arr1, arr2):
    lis = [ele for ele in arr1 if ele in arr2]
    return set(lis)

# Using set intersection()
def findCommon2(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common_values = set1.intersection(set2)
    return common_values

def findCommon3(arr1, arr2):
    common_values = np.intersect1d(arr1, arr2)
    return common_values

if __name__ == "__main__":
    arr1 = np.random.randint(low=0, high=10, size=10)
    arr2 = np.random.randint(low=0, high=10, size=10)
    
    res = list(findCommon(arr1, arr2))
    res2 = findCommon2(arr1, arr2)
    res3 = findCommon3(arr1, arr2)
    print(res)
    print(res2)
    print(res3)