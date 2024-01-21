# CONVERT NUM FROM INT REPRESENTATION TO STRING REPRESENTATION
def convertInt(x):
    if x == 0:
        return ''
    return convertInt(x // 10) + str(x % 10)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    res = convertInt(num)
    print(res)
    print(type(num))
    print(type(res))