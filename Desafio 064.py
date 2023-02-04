soma = pare = contador = 0
while pare != 999:
    num = int(input('Digite um número inteiro: '))
    soma += num
    contador += 1
    pare = int(input('Digite 999 caso deseja que o programa pare: '))
print('Você digitou {} números e a soma entre eles foi {} '.format(contador, soma))
