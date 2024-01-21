def main():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    print('\nOriginal: ', num1)
    print('Formatted: ' + '{:.2f}'.format(num1))
    print('\nOriginal: ', num2)
    print('Formatted: ' + '{:.2f}'.format(num2))

main()