soma = 0
pare = ''
media = 0
contador = 0
while pare != 'N':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    pare = str(input('Você deseja continuar [S/N]: ')).upper()
media = soma/contador
print('Você digitou {}valores e a média entre eles foi {}, o maior valor foi {} e o menor foi {}'.format(contador, media, maior, menor))
