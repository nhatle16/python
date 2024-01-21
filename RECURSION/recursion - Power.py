def findPower(a, b):
    if b == 0:
        return 1
    return a * findPower(a, b-1)

if __name__ == "__main__":
    base = int(input("Enter the base: "))
    expo = int(input("Enter the exponent: "))
    
    res = findPower(base, expo)
    print(res)