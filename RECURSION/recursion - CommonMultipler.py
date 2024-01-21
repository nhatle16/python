def commonDiv(a, b):
    low = min(a, b)
    high = max(a, b)
    
    if low == 0:
        return high
    elif low == 1:
        return 1
    return commonDiv(low, high%low)

def commonMul(a, b):
    return (a*b) // commonDiv(a, b)
    

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    gcd = commonDiv(num1, num2)
    lcm = commonMul(num1, num2)
    
    print(gcd)
    print(lcm)