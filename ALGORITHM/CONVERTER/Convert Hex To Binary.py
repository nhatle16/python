import re 

def check_hex(s):
    is_hex = bool(re.match("^[1-9A-F]+$",s))
    return is_hex

def convert_hex(hex_str):
    deci_num = int(hex_str,16)
    bi_num = bin(deci_num).replace("0b","")
    return bi_num

def main():
    hexNumber = input("Enter a hexadecimal number: ")
    if check_hex(hexNumber):
        res = convert_hex(hexNumber)

    print(res)

main()