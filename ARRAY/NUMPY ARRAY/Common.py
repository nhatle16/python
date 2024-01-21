import numpy as np

# 3x3x3 array with random values between 0 and 1
rand1 = np.random.rand(3,3,3)
print(rand1)

# 10x10 array with random values + find max and min 
rand2 = np.random.randint(10,51,size=(10,10))
print(rand2)
max_val = np.max(rand2)
min_val = np.min(rand2)
print(f"Max: {max_val}\n",
      f"Min: {min_val}")

# add 0's as border