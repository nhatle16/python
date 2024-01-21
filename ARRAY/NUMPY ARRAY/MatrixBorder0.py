import numpy as np

# Add border filled with 0's to existing matrix
def addBorder(mtrx):
    # defining new number of rows and cols
    new_rows = mtrx.shape[0] + 2
    new_cols = mtrx.shape[1] + 2
    
    # New matrix with new number of rows and cols
    new_mtrx = np.zeros(shape=(new_rows, new_cols),dtype=int)
    
    new_mtrx[1:-1, 1:-1] = mtrx
    
    return new_mtrx

if __name__ == "__main__":
    matrix = np.random.randint(low=1,high=10,size=(3,3))
    new_matrix = addBorder(matrix)
    print(new_matrix) 