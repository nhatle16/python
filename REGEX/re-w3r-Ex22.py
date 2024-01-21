import re

lis = ['hello','name','you']
text = "hello, nice to meet you, my name is Nolan"

for pattern in lis:
    match = re.search(pattern=pattern,string=text)
    s = match.start()
    e = match.end()
    print('Found "%s" from %d to %d' % (pattern, s, e))