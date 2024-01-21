# Checking order of character
# Using OrderedDict

from collections import OrderedDict

def check_order(s, pattern):
    # empty OrderedDict
    my_dict = OrderedDict.fromkeys(iterable=s)
    
    # traverse the OrderedDict and
    # pattern simultaneously
    
    # initialize a pointer to track 
    ptr = 0
    
    for key in my_dict.keys():
        if (key == pattern[ptr]):
            # increase if there is
            # a matched character
            ptr += 1
            
        if (ptr == len(pattern)):
            return True
        
    return False

if __name__ == "__main__":
    my_str = input("Type: ")
    pattern = input("Pattern: ")
    res = check_order(my_str, pattern)
    
    print(res)