import re

# Check if a string starts with a number 
def text_match(s):
    pattern = '^[0-9].*$'
    if re.search(pattern, s):
        print("Found")
    else:
        print("Not found")
        
# text_match('abc1012')
# text_match('1311Monday')

# Check if a string starts with a specific number
def text_match2(s):
    text = re.compile(r'^10')
    if text.match(s):
        print("Found")
    else:
        print("Not found")
        
text_match2('10-NHAT')
text_match2('16-LMN')