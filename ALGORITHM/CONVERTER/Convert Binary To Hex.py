import re

def check_bi(s):
    is_binary = bool(re.match("^[01]+$", s))
    return is_binary

def convert_to_hex(bi_str):
    # Add leading 0s to ensure the string length is multiple by 4
    while len(bi_str) % 4 != 0:
        bi_str = '0' + bi_str

    chart = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }

    hex_str = ""

    for i in range(0,len(bi_str),4):
        bi_group = bi_str[i:i+4]
        hex_digit = chart.get(bi_group)
        hex_str += hex_digit

    return hex_str

def main():
    binaryNum = input("Enter a binary number: ")
    if check_bi(binaryNum):
        res = convert_to_hex(binaryNum)
    
    print(res)

main()