my_list = [4, 5, 6, 7, 8, 9]

# 1: Using reverse method
def reverse1(my_list):
    my_list.reverse()
    return my_list

print(reverse1(my_list.copy()))

# 2: Using slicing technique
def reverse2(lis):
    new_lis = lis[::-1]
    return new_lis

print(reverse2(my_list))

# 3: Using defined function

def reverse3(lis):
    new_lis = lis
    if len(new_lis) == 1:
        return new_lis
    elif len(new_lis) == 2:
        new_lis[0], new_lis[1] = new_lis[1], new_lis[0]
    else:
        left = 0
        right = len(new_lis)-1
        while left <= right:
            new_lis[left], new_lis[right] = new_lis[right], new_lis[left]
            left += 1
            right -= 1
    return new_lis

print(reverse3(my_list.copy()))

# 4: Using list comprehension

def reverse4(lis):
    new_lis = [lis[len(lis) - i] for i in range(1,len(lis)+1)]
    return new_lis

print(reverse4(my_list))