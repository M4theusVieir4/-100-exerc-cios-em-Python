from random import randint
def sorteia(numeros):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]} ',end='')
    print('PRONTO!')

def somaPar(numeros):
    print(f'Somando os valores pares de {numeros}, temos ',end='')
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(soma)

numeros = []
sorteia(numeros)
somaPar(numeros)
