n = (float(input('Digite um número: ')),
    float(input('Digite outro número:')),
     float(input('Digite mais um número:')),
     float(input('Digite o último número:')))

print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 foi digitado pela primeira vez na posição {n.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado')
print('Números pares:', end='')
for c in n:
    if c % 2 == 0:
        print(c)
