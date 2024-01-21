from array import *
arr = array('i', [1,2,3,4,5])
print(arr)
print(f"Current memory address and length in elements of array: {arr.buffer_info()}")
print(f"Size of memory buffer in bytes: {arr.buffer_info()[1] * arr.itemsize}")