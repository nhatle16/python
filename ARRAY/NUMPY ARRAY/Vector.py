import numpy as np

# Create a null vector of size 10
null_v1 = np.zeros(10)
# print(null_v)

# Create a null vector of size 10 and fith element has value of 5
null_v2 = np.zeros(10)
null_v2[4] = 5
# print(null_v2)

# Vector with values ranging from 10 to 49 (inclusive)
vector = np.arange(10,50)
# print(vector)

# Reverse a vector
rev_vec = vector[::-1]
# print(rev_vec)

# Find indices of non-zero elements of vector
vector2 = np.array([1,2,0,0,4,0])
lis = [i for i in range(len(vector2)) if vector2[i] != 0]
# print(lis)

# Random vector of size 30 and find mean value
vector3 = np.random.randint(0,30,size=30)
mean_val = np.mean(vector3)
# print(vector3)
# print(mean_val)