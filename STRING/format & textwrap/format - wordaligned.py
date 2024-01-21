# right alignment with width 10
def right(num):
    print('Right aligned: ' + '{:>10d}'.format(num))

#left alignment with width 10
def left(num):
    print('Left aligned: ' + '{:<10d}'.format(num))

#center alignment with width 10
def center(num):
    print('Center alignment: ' + '{:^10d}'.format(num))

def main():
    n = int(input('Enter a number: '))
    right(n)
    left(n)
    center(n)

main()
