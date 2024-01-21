import re 

def check_bi(num):
    s = str(num)
    is_binary = bool(re.match("^[01]+$", s))
    return is_binary

def convert_to_dec(num):
    deci_num = 0
    pos = 0
    
    while num > 0:
        digit = num % 10 
        value = 2**pos
        deci_num += digit * value
        pos += 1
        num = num // 10

    return int(deci_num)

def main():
    lis = [10001,10110,11010,1011]

    for num in lis:
        if check_bi(num):
            res = convert_to_dec(num)
            print(res)
        else:
            print(f'{num} is not a binary number')

main()