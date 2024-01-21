def convert_dec(num):
    bi_num = bin(num).replace("0b", "")
    oct_num = oct(num).replace("0o", "")
    hex_num = hex(num).replace("0x", "")

    return bi_num, oct_num, hex_num

def main():
    number = int(input("Enter a number: "))
    binary, octal, hexa = convert_dec(number)

    print(binary)
    print(octal)
    print(hexa)

main()