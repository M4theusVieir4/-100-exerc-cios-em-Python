hei = float(input('Type your height in meters: '))
wei = float(input('Type your weight in kilogram:'))
imc = wei/(hei**2)
if imc < 18.5:
    print('weight below')
elif imc > 18.5 and imc < 25:
    print('ideal weight')
elif imc > 25 and imc < 30:
    print('overweight')
elif imc > 30 and imc < 40:
    print('obesity')
elif imc > 40:
    print('morbid obesity')
