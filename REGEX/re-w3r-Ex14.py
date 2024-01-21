import re

# Match a string that contains only upper and lowercase letters, numbers, 
# and underscores and has at least 1 character
def text_match(s):
    pattern = '^[A-Za-z0-9_]+$'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
text_match('NOlan1606')
text_match('Nolan1606')
text_match('&*(%)') 