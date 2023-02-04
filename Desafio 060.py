num = int(input('Digite um número:'))
i = 0
fat = 1
print('Calculando {}! ='.format(num), end='')
while i != num:
    i += 1
    fat *= i
print('O fatorial do número é {}'.format(fat))
