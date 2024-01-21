# Multiply 2 matrix with different size

import numpy as np

# @: operator to multiply 2 matrix
# .dot(): compute dot product (scalar product)

mtrxA = np.random.randint(low=0, high=10, size=(5,2))
mtrxB = np.random.randint(low=0, high=10, size=(2,3))

res1 = np.dot(mtrxA, mtrxB)
res2 = mtrxA @ mtrxB

print(res1)
print(res2)    