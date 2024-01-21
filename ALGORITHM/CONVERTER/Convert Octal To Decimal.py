import re

def check_oct(num):
    s = str(num)
    is_oct = bool(re.match("^[0-7]+$",s))
    return is_oct

def convert_oct(num):
    deci_num = 0
    pos = 0
    while num > 0:
        digit = num % 10
        value = 8**pos
        deci_num += value * digit
        pos += 1
        num = num // 10
    
    return deci_num

def main():
    num = 63
    if check_oct(num):
        res = convert_oct(num)
        print(res)

main()