from array import array

s = b'Minh_Nhat'
# Convert from bytes to normal string
new_str = s.decode('utf-8')
print(new_str)
# Convert from string to array
arr = array('i',[ord(char) for char in new_str])

for i in arr:
    print(i,end=' ')