# print number with a percentage
def percentage(n1):
    print('\nFormatted: ' + '{:%}'.format(n1))
    print('Formatted: ' + '{:.0%}'.format(n1)) # without decimal places
    print('Formatted: ' + '{:.2%}'.format(n1)) # rounded to 2 decimal places
    print()

def main():
    num = float(input('\nYour percent (smaller than 1): '))
    percentage(num)

main()