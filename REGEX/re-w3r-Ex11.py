import re

# Matchs a word at the end of string with optional punctuation 

def text_match(s):
    pattern = re.compile(r'\w+\S*$')
    if re.search(pattern=pattern, string=s):
        print("Found")
    else:
        print("Not found")
        
text_match('Hello Nolan CS!')
text_match('asdf16 ')
text_match('The Lonely Land?')