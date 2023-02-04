
print('\033[4;33m-=-'*20)
print('\033[mAnalyzer triangle')
print('\033[4;33m-=-'*20)
catA = float(input('\033[mType the value of cat A: '))
catO = float(input('Type the value of cat O:' ))
hip = float(input('Type the value of hypotenuse: '))
if hip < catA + catO and catA < hip + catO and catO < hip +catA:
    print('This segments can form a triangle')
else:
    print('This segments can not form a triangle')
