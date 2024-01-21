# read a string from a file then encode 
def CaesarCode(realText, step):
    outText = []    # List of words after encryption
    crypText = []   # List of words' index after encryption
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letter in realText:

        if letter in uppercase:
            idx = uppercase.index(letter)
            crypt = (idx + step) % 26 # always in alphabet
            crypText.append(crypt)
            word = uppercase[crypt]
            outText.append(word)

        elif letter in lowercase:
            idx = lowercase.index(letter)
            crypt = (idx + step) % 26
            crypText.append(crypt)
            word = lowercase[crypt]
            outText.append(word)
            
    return outText, crypText

def main():
    step = int(input('Enter step: '))
    with open('text.txt', 'r') as file:
        line = file.readline().strip()
    text, code = CaesarCode(line, step)
    print(text)
    print(code)

main()



