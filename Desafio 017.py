import math
op = float(input('Valor do cateto oposto:'))
adjacente = float(input('Valor do cateto adjacente'))
hipotenusa = math.sqrt(op**2 + adjacente**2)
print('O valor da hipotenusa é: {}'.format(hipotenusa))