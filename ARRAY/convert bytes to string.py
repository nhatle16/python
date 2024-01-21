from array import array

print("Bytes to string:")
x = array('b', [77,105,110,104,95,78,104,97,116])
s = x.tobytes()
y = array('b', [65,110,104,95,84,104,117])
z = y.tobytes()
s_str = s.decode('utf-8')
z_str = z.decode('utf-8')

print(s,z)
print(s_str, z_str)
print(type(s_str))