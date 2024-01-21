import re

sentence = "From nolan.16@usask.ca Sun Dec 10"

x = re.findall('\\S+@\\S+', sentence)
y = re.findall('(^From \\S+@.+?\\s)', sentence)

print(x)
print(y)