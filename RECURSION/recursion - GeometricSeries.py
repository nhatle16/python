# A geometric series is a series with a constant ratio between successive terms
def geometricSum(x):
    if x < 0:
        return 0
    return 1/pow(2,x) + geometricSum(x-1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    res = geometricSum(num)
    print(res)