import re

# re.findall(): find all occurrences of a pattern in a string and return them as a list of strings. 

pattern = "exercise"
text = "CMPT exercises, ECON exercises, MATH exercises"
lis = re.findall(pattern=pattern, string=text)

# for match in lis:
#     print('Found "%s"' % pattern)
    
for match in re.finditer(pattern=pattern, string=text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (pattern, s, e))