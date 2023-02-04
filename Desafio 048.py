print('-=-'*20)
print('Soma entre todos os números que são múltiplos de três e que se encontram no intervalo entre 1 até 500:')
soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma =+ c
print(soma)
