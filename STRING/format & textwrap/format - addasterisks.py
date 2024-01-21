# add asterisks to leading characters
def ast_left(n1, n2):
    print('\Original:', n1)
    print('Left padding formatted: ' + '{:*>3d}'.format(n1))
    print('Original:', n2)
    print('Left padding formatted: ' + '{:*>6d}'.format(n2))

def ast_right(n1, n2):
    print('\nOriginal:', n1)
    print('Right padding formatted: ' + '{:*<3d}'.format(n1))
    print('Original:', n2)
    print('Right padding formatted: ' + '{:*<6d}'.format(n2))

def main():
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))

    #ast_left(num1, num2)
    ast_right(num1, num2)

main()