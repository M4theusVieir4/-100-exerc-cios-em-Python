lista = []
count = 0
while True:
    valor = int(input('Digite um valor: '))
    count += 1
    if count == 1:
        lista.append(valor)
    if count == 2 and valor in lista:
        print('Valor duplicado não vou adcionar...')
    else:
        lista.append(valor)
        print('Valor adcionado com sucesso...')
    parada = str(input('Quer continuar [S/N]: ')).strip()[0]
    if parada != 'NnSs':
        parada = str(input('Digite uma resposta correta [S/N]: ')).strip()[0]
    if parada in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
