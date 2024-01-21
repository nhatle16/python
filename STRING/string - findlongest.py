word_list = []

num = int(input("Enter length of list: "))

for i in range(0, num):
    new_word =  input("Type a word: ")
    word_list.append(new_word)

def fineLongest(lis):
    length = 0
    word = ""
    for i in lis:
        if len(i) > length:
            length = len(i)
            word = i
    return length, word

length, word = fineLongest(word_list)

print(f"Longest word: {word}")
print(f"Length of longest word: {length}")