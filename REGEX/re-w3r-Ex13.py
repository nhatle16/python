import re

# Check if matches a word containing 'z', not the start or end of the word
def text_match2(s):
    pattern = re.compile(r'\Bz\B')
    if re.search(pattern=pattern, string=s):
        print("Matched")
    else:
        print("Not matched")   
             
text_match2('Im from New Zealand')
text_match2('You are crazy')
text_match2('Rizy hair')