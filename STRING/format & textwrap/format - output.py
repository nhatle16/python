def totalcost(q, p):
    total = p * q
    return total

def main():
    price = float(input('Price per item: '))
    quant = int(input('Quantities: '))

    paid = totalcost(quant, price)

    text = 'Your total cost is {money:.2f} dollars'
    print(text.format(money = paid))

main()

def print_text():
    text1 = "My name is {name}, I'm {age} years old"
    text2 = "It's {0} now, you should leave now {1}".format(10,'Nhat')
    text3 = "I have {:.2f} dollars and I bought {:.2f} dollars of snack".format(50.99, 30.49)
    text4 = "The balance in your account is ${:,} ".format(16000000)

    print(text1.format(name = 'Nhat', age = 19))
    print(text2.format(time = 10, name = 'Nhat'))
    print(text3)
    print(text4)

    
print_text()