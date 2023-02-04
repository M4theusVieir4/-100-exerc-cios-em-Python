ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input(f'Média de {ficha["nome"]} : '))
print(f'Nome é igual a {ficha["nome"]}')
print(f'Média é igual a {ficha["média"]}')
if ficha['média'] >= 7:
    ficha['situação'] = 'aprovado'
else:
    ficha['situação'] = 'reprovado'
print(f'Situação é igual a {ficha["situação"]}')