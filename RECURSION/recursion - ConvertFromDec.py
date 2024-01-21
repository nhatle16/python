def toBin(x):
    if x == 0:
        return ''
    return toBin(x // 2) + str(x % 2)

def toOct(x):
    if x == 0:
        return ''
    return toOct(x // 8) + str(x % 8)

def toHex(x):
    hex_str = "0123456789ABCDEF"
    if x == 0:
        return ''
    return toHex(x // 16) + hex_str[x % 16]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    bin_num = toBin(num)
    # oct_num = toOct(num)
    # hex_num = toHex(num)
    
    print(bin_num)
    # print(oct_num)
    # print(hex_num)