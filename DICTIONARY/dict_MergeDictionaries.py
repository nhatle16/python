dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

def merge_1(dic1, dic2):
    return dic1.update(dic2)
    
def merge_2(dic1, dic2):
    res = {**dic1, **dic2}
    return res

# This returns None
print(merge_1(dict1, dict2))

print(dict1)
print(merge_2(dict1, dict2))