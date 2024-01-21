from array import *

a = array('i',[1,2,5,4,6,3,9])
# THERE IS NO COPY(), CLEAR(), SORT() FOR ARRAY

# Method append()
a1 = a
a1.append(9)
print(a1, '\n')

# Method insert()
a2 = a
a2.insert(2,4)
print(a2, '\n')

# Method extend()
lis = [1,6,0]
a3 = a
a3.extend(lis)
print(a3,'\n')

# Method index()
print(a.index(4),'\n')

# Method count()
print(a.count(2),'\n')

# Method pop()
a4 = a
a4.pop()
print(a4,'\n')

# Method remove()
a5 = a
a5.remove(2)
print(a5,'\n')

# Method reverse()
a6 = a
a6.reverse()
print(a6,'\n')