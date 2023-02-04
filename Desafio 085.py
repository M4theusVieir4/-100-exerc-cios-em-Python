
total = [[], []]
valor = 0
for c in range(0, 7):
    v = (int(input(f'Digite o {c + 1}º valor: ')))
    if v % 2 == 0:
        total[0].append(v)
    else:
        total[1].append(v)
total[0].sort()
total[1].sort()

print(f'Os valores pares digitados foram: {total[0]}')
print(f'Os valores ímpares digitados foram: {total[1]}')

