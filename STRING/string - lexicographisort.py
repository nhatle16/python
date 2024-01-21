str1 = input('Enter a string: ')
str2 = input('Enter a string: ')

def lexicographi_sort(s):
    return sorted(s) # no distinguish between upper and lower case
    # return sorted(sorted(s), key=str.upper) # distinguish between upper and lower
print(lexicographi_sort(str1))