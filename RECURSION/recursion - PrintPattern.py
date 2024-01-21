def printPattern(num):
    if num <= 0:
        print(num, end=' ')
        return 
    print(num, end=' ')
    printPattern(num-5)
    print(num, end=' ')
    
printPattern(17)