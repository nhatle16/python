from array import array

def max_pair(arr):
    l = len(arr)
    if l < 2:
        return -1
    
    x,y = arr[0], arr[1]
    
    for i in range(l-1):
        for j in range(i+1, l):
            if arr[i] * arr[j] > x * y:
                x, y = arr[i], arr[j]
                
    return (x,y)

a = array('i', [-1,3,6,-4,-9,3,8,2])
print(f"Max product pair: {max_pair(a)}")