import re

def text_match(s):
    newstr = re.sub(pattern=r'\.[0]*', repl='.', string=s)
    return newstr
s1 = "216.08.094.196"

def text_match2(s):
    newstr = re.sub(pattern=r'\b0*(\d+)\b', repl=r'\1', string=s)
    return newstr

s2 = "001012.1606.00.03.04.2023"

print(text_match(s1))
print(text_match2(s2))