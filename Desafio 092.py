from datetime import datetime
ficha = dict()
ficha['nome'] = str(input('Nome: '))
nascimento = int(input('Data de nascimento: '))
data = datetime.now().year - nascimento
ficha['idade'] = data
ficha['CTPS'] = int(input('Carteira de trabalho [0 não tem]: '))
if ficha['CTPS'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$ '))

ficha['aposentadoria'] =  35 - ficha['contratação'] + datetime.now().year + ficha['idade']
print(ficha)
print('-='*30)
for k,v in ficha.items():
    print(f'{k} tem o valor {v}')


