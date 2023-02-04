tabuada = float(input('Digite um número para ver sua tabuada:'))
limite = int(input('Digite até onde você quer q a tabuada vá:'))
print('O número que será mostrado a tabuada é: {} até {}'.format(tabuada, limite))
print('-=-'*20)
for c in range(0,limite + 1):
    multiplicação = tabuada*c
    print('{} X {} = {}'.format(tabuada, c, multiplicação))

