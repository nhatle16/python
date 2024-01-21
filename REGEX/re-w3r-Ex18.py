import re

# re.compile(): Compile a regular expression pattern into a regex object
# re.finditer(): Find all occurrences of a pattern in a string and return an iterator yielding match objects for each match. 

def text_match(s):
    pattern = re.compile(pattern=r'\d{1,3}')
    res = re.finditer(pattern=pattern, string=s)
    for i in res:
        print(i.group())
        
text_match("Exercises number 1, 12, 13, and 345 are important")