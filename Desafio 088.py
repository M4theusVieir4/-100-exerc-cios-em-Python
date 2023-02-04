from random import randint
from time import sleep
print('-'*30)
print('     JOGA NA MEGA SENA       ')
print('-'*30)
listas = []

jogos = []
quant = int(input('Quantas jogos deseja sortear?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(0, 60)
        if n not in listas:
            listas.append(n)
            cont += 1
        if cont >= 6:
            break
    jogos.append(listas[:])
    listas.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-='*5,'<BOA SORTE!>','-='*5)




