import re 

def check_oct(s):
    is_oct = bool(re.match("^[0-7]+$",s))
    return is_oct

def convert_to_bi(oct_str):
    chart = {
        "0": "000", "1": "001", "2": "010", "3": "011",
        "4": "100", "5": "101", "6": "110", "7": "111"
    }

    bi_str = ""

    for num in oct_str:
        digit = chart.get(num)
        bi_str += digit

    return bi_str

def main():
    octalNumber = input("Enter an octal number: ")
    if check_oct(octalNumber):
        res = convert_to_bi(octalNumber)
    
    print(res)

main()