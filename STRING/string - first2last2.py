my_str = input("Enter a string: ")

def createString(newstr):
    if len(newstr) <= 2:
        return ""
    else:
        res = newstr[0:2] + newstr[-2:]
        return res

print(createString(my_str))