my_string = input("Enter a string: ")

while my_string.count(" ") == 0:
    my_string = input("Enter a string: ")

def swapFirst2(newstr):
    # the string has 2 words
    part1 = newstr.split(" ")[0]
    part2 = newstr.split(" ")[1]

    str1 = part2[0:2] + part1[2:]
    str2 = part1[0:2] + part2[2:]

    print(str1, str2)

swapFirst2(my_string)