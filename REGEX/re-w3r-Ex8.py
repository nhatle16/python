import re

def text_match(s):
    pattern = re.compile(r'[A-Z]+[a-z]+')
    if re.search(pattern=pattern, string=s):
        print("Found")
    else:
        print("Not found")
        
text_match("AAaTtHhUu")
text_match("aA")
text_match("A")
text_match("Aaa")