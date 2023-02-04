from datetime import date
tot = 0
acu = 0
tempo = date.today().year
for c in range(1, 8):
    idade = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    if tempo - idade >= 18:
        tot += 1
    else:
        acu += 1

print('Existem {} pessoas maiores de idade e {} pessoas menores de idade'.format(tot, acu))