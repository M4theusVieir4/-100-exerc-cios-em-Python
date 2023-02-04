perfil = dict()
perfil['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {perfil["nome"]} jogou? '))
gols = []
tot = 0
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p}: ')))
    tot += gols[p]
perfil['gols'] = gols[:]
perfil['total'] = tot
print('-='*30)
print(perfil)
print('-='*30)
for k, v in perfil.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {perfil["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'    => Na partida {p}, fez {perfil["gols"][p]} gols.')
print(f'Foi um total de {perfil["total"]} gols.')
