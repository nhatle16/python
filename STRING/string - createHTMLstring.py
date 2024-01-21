title = 'welcome to the program'
tag = input('Type in a tag: ')

def addTags(tags, title):
    res = title.title()
    open = '<' + tags + '>'
    close = '</' + tags + '>'
    res = open + res + close
    return res

def addTags2(tags, title):
    res = '<%s>%s</%s>'% (tags,title,tags)
    return res

print(addTags(tag, title))
print(addTags2(tag, title))