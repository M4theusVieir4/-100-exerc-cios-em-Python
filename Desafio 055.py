maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {} pessoa:'.format(pessoa)))
    if pessoa ==1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('''O maior peso lido foi {}:
e o menor peso lido foi {}'''.format(maior, menor))