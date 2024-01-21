def main():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('\n Two decimal places\n')
    print('\nOriginal: ', num1)
    print('2 decimal places signed: ' + '{:+.2f}'.format(num1))
    print('No decimal places: ' + '{:.0f}'.format(num1))
    print('\nOriginal: ', num2)
    print('2 decimal places signed: ' + '{:+.2f}'.format(num2))
    print('No decimal places: ' + '{:.0f}'.format(num2))

main()