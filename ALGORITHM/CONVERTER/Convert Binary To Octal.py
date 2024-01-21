import re

def check_bi(num):
    s = str(num)
    is_binary = bool(re.match("^[01]+$", s))
    return is_binary

def convert_to_octal(bi_str):
    while len(bi_str) % 3 != 0:
        bi_str = '0' + bi_str
    
    chart = {
        "000": "0", "001": "1", "010": "2", "011": "3",
        "100": "4", "101": "5", "110": "6", "111": "7",
    }

    oct_str = ""

    for i in range(0,len(bi_str),3):
        bi_group = bi_str[i:i+3]
        digit = chart.get(bi_group)
        oct_str += digit

    return oct_str

def main():
    binaryNumber = input("Enter a binary number: ")
    if check_bi(binaryNumber):
        res = convert_to_octal(binaryNumber)

    print(res)

main()