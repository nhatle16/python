# Normalize a matrix
# Using min-max scaling: Difference between each entry and the smallest entry divided
#                        by the difference between largest entry and smallest entry

import numpy as np

def normalizeMatrix(mtrx):
    max_val = np.max(mtrx)
    min_val = np.min(mtrx)
    diff = max_val - min_val
    
    norm_mtrx = (mtrx - min_val) / diff
    
    return norm_mtrx

if __name__ == "__main__":
    matrix = np.random.randint(low=1, high=20, size=(5,5))
    res = np.round(normalizeMatrix(matrix),2)
    print(matrix)
    print(res)