n = mult = 0
while True:
    n = int(input('Digite um número(Negativo caso deseje encerrar o programa):'))
    if n < 0:
        break
    for c in range(0, 11):
        mult = n
        mult *= c
        print(f'{n} X {c} = {mult} ...', end= '')
print('Tabuada encerrada')
