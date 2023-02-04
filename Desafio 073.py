times = ('Palmeiras', 'Flamego', 'Fluminense', 'Corinthians', 'Internacional', 'Atletico-PR',
'Atlético MG', 'Santos', 'América-MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará SC',
'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print('-='*30)
print(f'Lista dos times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros colocados do Brasileirão são: {times[0:5]}')
print('-='*30)
print(f'Os G4 da lanterna são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print('O Corinthians está na posição : ',end='')
print(times.index('Corinthians')+1)
