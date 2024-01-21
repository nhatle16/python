import re 

# Find sequences of lowercase letters joined by an underscore

def text_match(s):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    if re.search(pattern=pattern, string=s):
        print("Matched")
    else:
        print("Not matched")
        
text_match('athu_athu')
text_match('lmn_123')
text_match('lmn_athu')
text_match("The string that has the form abc_abc is accepted")