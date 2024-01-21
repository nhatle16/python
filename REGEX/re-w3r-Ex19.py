import re

def text_match(s, lis):
    for pattern in lis:
        print("Searching for '%s' in '%s'" % (pattern, s))
        if re.search(pattern=pattern, string=s):
            print("Found!")
        else:
            print("Not found!")
            
text = "The quick brown fox jumps over the lazy dog"
lis = ['fox', 'over', 'dog']

text_match(text, lis)