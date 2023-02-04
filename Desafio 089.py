cont = 0
ficha = []
r = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/2
    r = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    ficha.append([nome,[nota1, nota2], média])
    cont += 1
    if r in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome:":<10}{"Media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)
while True:
    opc = int(input('Deseja ver a nota de qual aluno?(999 interrompe): '))
    if 999 != opc:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        break
    print('-'*30)
print('Finalizando...')
print('<<< VOLTE SEMPRE >>>')