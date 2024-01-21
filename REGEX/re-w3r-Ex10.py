import re

def text_match(s):
    pattern = re.compile('^[a-z].*$')
    if re.search(pattern, s):
        print("Matched")
    else:
        print("Not matched")
        
text_match('aatthhuu')
text_match('lmn1606')
text_match('13/11/2023')