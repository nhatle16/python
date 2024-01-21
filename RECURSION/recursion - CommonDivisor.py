def commonDiv(a, b):
    low = min(a, b)
    high = max(a, b)
    
    if low == 0:
        return high
    elif low == 1:
        return 1
    
    # print(low, high)
    return commonDiv(low, high%low)

if __name__ == "__main__":
    num = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    res = commonDiv(num, num2)
    print(res)