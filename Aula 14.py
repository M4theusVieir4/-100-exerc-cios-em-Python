'''for c in range(1, 10):
    print(c)
print('fim')'''
'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Deseja continuar? [S/N]: ')).upper()'''
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor inteiro'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))