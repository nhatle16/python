import re

pattern = "fox"
text = "The quick brown fox jumps over the lazy dog"
match = re.search(pattern=pattern, string=text)
s = match.start()
e = match.end()

print("Found %s in %s, from %s to %s" % (pattern, text, s, e))