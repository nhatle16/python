def check_pattern(color, pattern):
    if len(color) != len(pattern):
        return False
    
    sdict = {}
    pset = set()
    cset = set()
    
    for i in range(len(pattern)):
        pset.add(pattern[i])
        cset.add(color[i])
        if pattern[i] not in sdict.keys():
            sdict[pattern[i]] = []
            
        keys = sdict[pattern[i]]
        keys.append(color[i])
        sdict[pattern[i]] = keys
    
    if len(pset) != len(cset):
        return False
    for values in sdict.values():
        for i in range(len(values)-1):
            if values[i] != values[i+1]:
                return False
    
    return True

color = ['red','green','red','yellow']
pattern = ['a','b','a','c']

print(check_pattern(color, pattern))