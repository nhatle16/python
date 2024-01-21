from array import array

def swap_part(arr, pos):
    pos = pos % len(arr)
    return arr[-pos:] + arr[:-pos]

arr = array('i', [1,3,4,5,6,0,9,8,2])
pos = 2

print(swap_part(arr,pos))