def countDigits(n):
    if n == 0:
        return 0
    return 1 + countDigits(n // 10)

if __name__ == "__main__":
    print(countDigits(12345))