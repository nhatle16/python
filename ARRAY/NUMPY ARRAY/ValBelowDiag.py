# Insert value just below diagonal

import numpy as np

def insertBelow(mtrx, lis):
    count = 0
    dimension = mtrx.shape[0]
    for i in range(1,dimension):
        for j in range(dimension-1):
            if j >= i:
                pass
            elif i-1 == j:
                mtrx[i, j] = lis[count]
                count += 1
    
    return mtrx

if __name__ == "__main__":
    matrix = np.zeros(shape=(5,5),dtype=int)
    lis = []
    
    while len(lis) < matrix.shape[0]-1:
        val = int(input('Enter value: '))
        lis.append(val)

    res = insertBelow(matrix, lis)
    print(res)