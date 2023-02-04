idade_maior = homens = mulheres_jovens = 0
while True:
    print('     Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        idade_maior += 1
    if sexo == 'M':
        homens += 1
    if sexo =='F' and idade < 20:
        mulheres_jovens +=1
    print('-'*30)
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-'*30)
    if resposta == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos : {idade_maior}
Ao todo temos {homens} homens cadastrados
E temos {mulheres_jovens} mulher com menos de 20 anos''')

