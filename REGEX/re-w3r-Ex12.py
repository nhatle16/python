import re

# Check if string has a word containing 'z' and follow by other character
def text_match(s):
    pattern = re.compile(r'\w*z.\w*')
    if re.search(pattern=pattern, string=s):
        print("Matched")
    else:
        print("Not Matched")
        
# text_match('abczxy')
# text_match('abcxyz')
# text_match('zela')
# text_match("The quick brown fox jumps over the lazy dog.")