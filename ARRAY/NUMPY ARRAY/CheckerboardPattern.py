# Filled a matrix with checkerboard pattern

import numpy as np

# np.tile() : constructing an array by repeating A by 'reps' times

def checkerCreate(mtrx):
    # Fill even rows and odd cols with 1
    mtrx[0::2, ::2] = 1
    # Fill odd rows and even cols with 1
    mtrx[1::2, 1::2] = 1
    return mtrx

def checkerboardTile():
    # Create 8x8 checkerboard pattern
    # matrix with tile function
    mtrx = np.array([[1,0],[0,1]])
    c_board = np.tile(A=mtrx, reps=(4,4))
    return c_board

if __name__ == "__main__":
    matrix = np.zeros(shape=(8,8), dtype=int)
    res = checkerCreate(matrix)
    # print(res)
    
    res2 = checkerboardTile()
    print(res2)