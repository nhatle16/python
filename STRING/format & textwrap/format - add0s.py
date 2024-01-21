# add 0s to the leading characters
def add_0sleft(n1, n2):
    print('\nOriginal:', n1)
    print('Left padding formatted, width 2: ' + '{:0>2d}'.format(n1))
    print('Original: ', n2)
    print('Left padding formatted, width 6: ' + '{:0>6d}'.format(n2))

# add 0s to the trailing characters
def add_0sright(n1, n2):
    print('\nOriginal:', n1)
    print('Right padding formatted, width 2: ' + '{:0<2d}'.format(n1))
    print('Original:', n2)
    print('Right padding formatted, width 6: ' + '{:0<6d}'.format(n2))

def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    add_0sleft(num1, num2)
    add_0sright(num1, num2)


main()
