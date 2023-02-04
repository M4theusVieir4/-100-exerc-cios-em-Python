galera = list()
dados = list()
total = maior = menor =  0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    elif maior < dados[1]:
        maior = dados[1]
    elif menor > dados[1]:
        menor = dados[1]

    galera.append(dados[:])
    dados.clear()
    r = (str(input('Quer continuar? [S/N]: '))).strip()[0]
    if r in 'Nn':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas')

print(f'O maior peso contabilizado foi {maior} kg de ',end ='')
for p in galera:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso contabilizado foi {menor} kg de ',end ='')
for p in galera:
    if p[1] == menor:
        print(p[0])

