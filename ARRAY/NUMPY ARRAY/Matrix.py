import numpy as np

# 3x3 matrix with values ranging from 0 to 8
matrix1 = np.arange(9).reshape(3,3)
# print(matrix1)

# 3x4 matrix with values ranging from 12 to 24
matrix2 = np.arange(12,24).reshape(3,4)
# print(matrix2)

# 4x4 matrix with values ranging from 0 to 32, step is 2
matrix3 = np.arange(0,32,2).reshape(4,4)
# print(matrix3)

# 3x3 identity matrix
matrix4 = np.eye(3)
# print(matrix4)

# 5x5 matrix with 1 on the border and 0 inside
matrix5 = np.zeros(shape=(5,5))
matrix5[0,:] = 1
matrix5[-1,:] = 1
matrix5[:,0] = 1
matrix5[:,-1] = 1
# print(matrix5)

# 5x5 matrix with 1 on the border and 0 inside
matrix6 = np.ones(shape=(5,5))
matrix6[1:-1, 1:-1] = 0
#print(matrix6)

# 5x5 matrix with 1,2,3,4 below the diagonal
matrix7 = np.zeros(shape=(5,5),dtype=int)
values = [1,2,3,4]
np.fill_diagonal(a=matrix7[1:], val=values)
print(matrix7)

print(matrix7.flatten)