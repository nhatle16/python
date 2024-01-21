# Negate elements under specific conditions

import numpy as np

# np.copy(): create a copy of original array
# np.logic_and(): perform element_wise logic AND operation 

def negateMatrix(arr, a, b):
    # determine indices to be negated
    new_arr = np.copy(arr)
    negate_indices = np.logical_and(new_arr > a,new_arr < b)
    # negate elements 
    new_arr[negate_indices] = -new_arr[negate_indices]
    print(np.logical_and(new_arr > a,new_arr < b))
    return new_arr

if __name__ == "__main__":
    arr = np.random.randint(low=0, high=10, size=(10))
    res = negateMatrix(arr,3,8)
    print(arr)
    print(res)