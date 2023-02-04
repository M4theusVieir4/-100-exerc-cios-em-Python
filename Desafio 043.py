value = float(input('Type the value of the product'))
condition = int(input('What is the payment condition? you have this options: in cash(press 1) / in sight on the card (press2) / 2x in card (press 3) / 3x or more in card (press 4)'))
if condition == 1:
    print('The value of product is {}'.format(value - value*10/100))
elif condition == 2:
    print('The value of product is {}'.format(value - value*5/100))
elif condition == 3:
    print('The value of product is {}'.format(value))
elif condition == 4:
    print(' The value of product is {}'.format(value + value*20/100))
    
