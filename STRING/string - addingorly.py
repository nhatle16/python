my_string = input("Type in a string: ")

def addPostfix(newstr):
    res = newstr
    if len(res) < 3:
        pass
    elif newstr[-3:] == "ing":
        res += "ly"
    else:
        res += "ing"
    return res

print(addPostfix(my_string))
