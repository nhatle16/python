my_str = input("Type in a string: ")

def countChar(newstr):
    dict = {}
    for i in newstr:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(countChar(my_str))