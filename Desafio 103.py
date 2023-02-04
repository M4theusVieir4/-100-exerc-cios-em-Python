def ficha(n='<desconhecido>', g='O'):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')

#Função Principal
nome= str(input('Nome do jogador: '))
gols= str(input('Número de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)


