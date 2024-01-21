from array import array

def check_lost(nums):
    lis = []
    for i in range(10,20+1):
        if i not in nums:
            lis.append(i)
            
    return lis

ar1 = array('i', [11,13,14,16,17,19,20]) 
res1 = check_lost(ar1)

print(f"Missing numbers in (10-20) is: {res1}")