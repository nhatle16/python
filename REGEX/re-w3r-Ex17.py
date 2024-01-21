import re

# re.match(): Check for a match only from beginning of a string, implicitly include '^'
#             return a match object if the pattern is found, otherwise return None

# re.search(): Scans the entire string for a match and returns the first occurrence,
#              otherwise return None. It can match anywhere in the string

def text_match(s):
    pattern = ".*[0-9]$"
    if re.search(pattern, s):
        return True
    else:
        return False
    
def text_match2(s):
    text = re.compile(r'.*[0-9]$')
    if text.match(s):
        return True
    else:
        return False
    
print(text_match('1606lmn'))
print(text_match('lmn1606'))