import array as arr

def remove_duplicate(nums):
    return sorted(set(nums), key=nums.index)

ar1 = arr.array('i', [1,3,3,5,6,1,9])
ar2 = arr.array('i',[2,4,6,8,4,2,7,3])

res1 = arr.array('i', remove_duplicate(ar1))
res2 = arr.array('i', remove_duplicate(ar2))

print("Original array:")
for i in ar1:
    print(i, end=' ')
    
print("\nResult:")
for i in res1:
    print(i, end=' ')
print()
print("\nOriginal array:")
for i in ar2:
    print(i, end=' ')
    
print("\nResult:")
for i in res2:
    print(i, end=' ')