from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = list()
print('valores sorteados:')
for j in range(0, 4):
    dados[f'jogador {j}'] = randint(1, 6)
    print(f'O jogador {j + 1} tirou {dados[f"jogador {j}"]}.')
    sleep(1)
print('Ranking dos jogadores: ')
ranking = sorted(dados.items(), key = itemgetter(1), reverse = True)
print(ranking)
for i, v in enumerate(ranking):
    print(f' {i + 1}ª lugar:  {v[0]} com {v[1]}.')
    sleep(1)

