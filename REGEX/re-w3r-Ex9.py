import re

def text_match(s):
    pattern = 'a.*?b$'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
text_match('axasdb')
text_match('aatthhuu')