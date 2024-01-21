str1 = input('Type in a string: ')

def not_poor(mystr):
    inot = mystr.find('not')
    ipoor = mystr.find('poor')

    if ipoor > inot and ipoor > 0 and inot > 0:
        mystr = mystr.replace(mystr[inot:ipoor+4], 'good')
        return mystr
    else:
        return mystr
    
print(not_poor(str1))