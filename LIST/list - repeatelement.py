lis = [3,6,4,2,7]
num = int(input("Enter a repetition value: "))

# 1: Using list comprehension
def repeat1(lis, n):
    res1 = [ele for idx, ele in enumerate(lis) for i in range(n) if idx % 2 == 0]
    return res1

print(repeat1(lis, num))

# 2: Using extend() and "*" operator

def repeat2(lis, n):
    res2 = []
    for i in range(0,len(lis)):
        if i % 2 == 0:
            res2.extend([lis[i]] * n)
    return res2

print(repeat2(lis, num))

# 3: Using extend() and slicing 
def repeat3(lis, n):
    sliced = lis[::n]
    res3 = []
    for i in range(0,len(sliced)):
        res3.extend([sliced[i]] * n)
    return res3

print(repeat3(lis, num))

