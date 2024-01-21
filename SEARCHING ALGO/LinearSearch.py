def search(arr, N, x): 
  
    for i in range(0, N): 
        print(arr[i])
        if (arr[i] == x): 
            return i 
        
    return -1

arr = [12, 17, 20, 25, 25, 30, 42, 42, 42, 50, 50, 63, 75, 80, 87, 99]
print(search(arr, len(arr), 77))