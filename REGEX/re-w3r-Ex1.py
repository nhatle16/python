import re

def check(s):
    charRe = re.compile(r'^[a-zA-Z0-9]+$')
    if re.search(pattern=charRe, string=s):
        return True
    else:
        return False

s = "Nolan1606"
s2 = "!abc16_cs"
print(check(s))
print(check(s2))