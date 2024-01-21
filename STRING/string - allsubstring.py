my_str = input("Enter a string: ")

def subString(new_str):
    length = len(new_str)
    count = 0
    for i in range(0, length):
        for j in range(i+1, length+1):
            print(new_str[i:j])
            count += 1
    print(f"Total substrings: {count}")

subString(my_str)