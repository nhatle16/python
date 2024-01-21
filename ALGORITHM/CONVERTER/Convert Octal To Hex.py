import re

def check_oct(s):
    is_oct = bool(re.match("^[0-7]+$",s))
    return is_oct

def convert_to_hex(oct_num):
    dec_num = int(oct_num, 8)
    hex_num = hex(dec_num).replace("0x","").upper()
    print (hex_num)

def main():
    convert_to_hex('5123')

main()