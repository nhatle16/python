import re 

def check_hex(s):
    is_hex = bool(re.match("^[0-9A-F]+$", s))
    return is_hex

def convert_hex(s):
    hex_char = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    deci_num = 0
    l = len(s)
    pos = l-1
    for i in range(l):
        digit = 0

        if s[i] in hex_char.keys():
            digit = hex_char[s[i]]
        else:
            digit = int(s[i])

        value = 16**pos
        deci_num += value * digit
        pos -= 1

    return deci_num

def main():
    hexNumber = input("Enter a hexadecimal number: ")
    if check_hex(hexNumber):
        res = convert_hex(hexNumber)
        
    print(res)

main()