lista = []
par = []
ímpar = []
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    parada = str(input('Quer continuar? [S/N]:')).strip()[0]
    if valor % 2 == 0:
        par.append(valor)
    else:
        ímpar.append(valor)
    if parada not in 'SsNn':
        parada = str(input('Escreva uma opção correta [S/N]: ')).strip()[0]
    if parada in 'Nn':
        break
print('-='*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')
