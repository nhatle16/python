import re 

def check_hex(s):
    is_hex = bool(re.match("^[0-9A-F]+$",s))
    return is_hex

def convert_hex(hex_str):
    deci_num = int(hex_str, 16)
    oct_num = oct(deci_num).replace("0o", "")
    return oct_num

def main():
    hexNumber = input("Enter a hexadeciaml number: ")
    if check_hex(hexNumber):
        res = convert_hex(hexNumber)

    print(res)

main()