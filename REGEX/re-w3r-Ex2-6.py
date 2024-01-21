import re 

# # 0 or more Bs follow A 
def NoOrMoreB(s):
    pattern = '^a(b*)$'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
        
# NoOrMoreB('ab')
# NoOrMoreB('abc')
# NoOrMoreB('abb')
# NoOrMoreB('bab')
# NoOrMoreB('acb')

# # 1 or more Bs follow A
def OneOrMoreB(s):
    pattern = '^a(b+)$'
    if re.match(pattern, s):
        print("Found")
    else:
        print("Not found")
        
# OneOrMoreB('abb')
# OneOrMoreB('ab')
# OneOrMoreB('ac')
# OneOrMoreB('a')

# # 3 Bs follow A
def ThreeB(s):
    pattern = 'ab{3}'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
# ThreeB('ab')
# ThreeB('abbb')
# ThreeB('abbcc')
# ThreeB('abbbb')

# # 0 or 1 B follows A
def NoOrOneB(s):
    pattern = 'ab?'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
# NoOrOneB('ab')
# NoOrOneB('a')
# NoOrOneB('abb')

# # 2 or 3 Bs follow A
def TwoOrThreeB(s):
    pattern = 'ab{2,3}'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
# TwoOrThreeB('ab')
# TwoOrThreeB('abb')
# TwoOrThreeB('abbc')
# TwoOrThreeB('abbb')