lista = []
count = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    count += 1
    lista.sort(reverse = True)
    
    parada = str(input('Quer continuar [S/N]: ')).strip()[0]
    if parada in 'Nn':
        break
print(f'Você digitou {count} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 foi digitado na lista')
else:
    print('O número 5 não está na lista')
