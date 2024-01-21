# Print rightward solid pyramid
def rightSolidPyra(n):
    # Number of spaces:
    k = 2*n - 2
    for i in range(n):
        for j in range(k):
            print(' ', end='')
        k = k-2
        for j in range(0, i+1):
            print('* ', end='')
        print()

# Print leftward solid pyramid
def leftSolidPyra(n):
    for i in range(n):
        for j in range(0,i+1):
            print('* ', end='')
        print()

# Print leftward reversed pyramid
def revLeftPyra(n):
    for i in range (n):
        for j in range(n-i):
            print('* ', end='')
        print()

# Print rightward reversed pyramid
def revRightPyra(n):
    # Number of spaces
    k = 0
    for i in range(n):
        for j in range(k):
            print(' ', end='')
        k += 2
        for j in range(i, n):
            print('* ', end='')
        print()

# Print reversed equilateral pyramid 
def revEquiPyra(n):
    for i in range(n, 0, -1):
        for j in range(0, n-i):
            print(' ', end='')
        for j in range(i):
            print('* ', end='')
        print()

# Print equilateral pyramid
def equiPyra(n):
    for i in range(0, n):
        for j in range(0, n-i-1):
            print(' ', end='')
        for j in range(i+1):
            print('* ', end='')
        print()

def main():
    num = int(input("Enter size: "))
    # leftSolidPyra(num)
    # rightSolidPyra(num)
    # revLeftPyra(num)
    # revRightPyra(num)
    equiPyra(num)
    revEquiPyra(num)
main()