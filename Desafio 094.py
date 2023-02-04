pessoa = dict()
registro = list()
mulheres = list()
r = ''
tot = media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    tot += 1
    registro.append(pessoa.copy())
    r = str(input('Deseja continuar? [S/N]')).strip()[0]
    if r in 'Nn':
        break
media += soma/tot
print('-='*30)
print(f'- O grupo tem {tot} pessoas.')
print(f'- A média de idade é {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista das pessoas que estão acima da média:')
print(registro)
media += soma/tot
for p in registro:
    if p['idade'] >= media:
        print('     ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<Encerrado>>')




