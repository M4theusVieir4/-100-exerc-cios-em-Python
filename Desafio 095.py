jogador = dict()
gols = list()
ficha = list()
print('-'*30)
r = ''
tot = 0
while True:
    tot = 0
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for j in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {j}?')))
        tot += gols[j]
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    ficha.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if r in 'SN':
            break
    if r in 'N':
        break

print(ficha)
print('-='*30)
print(f"{'cod nome':<20}{'gols':<10}{'total':>20}")
print('-'*60)
for e in ficha:
    print(f'{e} ',end='')
    for k, v in e.items():
        print(f'{k:<20}{v:<10}', end ='')
    print()
