my_str = input("Enter a sentence: ")

def countWord(sen):
    dict = {}
    words = sen.split() # splits string at white space into a list of words
    for n in words:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(countWord(my_str))