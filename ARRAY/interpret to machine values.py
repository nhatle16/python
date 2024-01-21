from array import array
import binascii

arr1 = array('i', [1,6,9,2,5])
print(f"array1: {arr1}")

# Convert to bytes
arr = arr1.tobytes()
# arr3 = bytes(arr1)

# Convert from binary to hexadecimal representation
print(f"Hex representation: {binascii.hexlify(arr)}")

# Create array from machine values
arr2 = array('i')   
arr2.frombytes(arr)
print(f"array2: {arr2}")