from random import randint
cont = maior = menor =0
for c in range(0,5):
    número = randint(0,10)
    tupla = (número)
    print(f'→{tupla}  ', end ='')
    cont += 1
    if cont == 1:
        maior = menor = número
    elif maior < número:
        maior = número
    elif menor > número:
        menor = número
print(f'\n O maior número da tupla é {maior} e o menor número da tupla é {menor}')