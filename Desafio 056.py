media = 0
soma= 0
velho = 0
name = ''
tot = 0
for pessoa in range(1,5):
    print('-----------{}º Pessoa --------'.format(pessoa))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]: ')).upper()
    soma += idade
    media = soma/pessoa
    if velho < idade:
        velho = idade
        name = nome
    if sexo == 'F' and idade < 20:
        tot += 1

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {} '.format(velho, name))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot))