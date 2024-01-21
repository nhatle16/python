def sumAllDigits(num):
    if num == 0:
        return 0
    digit = num % 10
    return digit + sumAllDigits(num//10)

print(sumAllDigits(1234567))