#pessoas = {'nome': 'Matheus', 'sexo':'M' , 'idade': 20}
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem  {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome']='Leandro'
#pessoas['peso']= 98.5
#for k, v in pessoas.items():
   # print(f'{k} = {v}')
#brasil = []
#estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
#estado2 = {'uf':'São Paulo','sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Escreva um estado: '))
    estado['sigla'] = str(input('Escreva a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

