maior = menor = 0
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}:')))
    if v == 0:
        maior = menor = valores[v]
    if maior < valores[v]:
        maior = valores[v]

    if menor > valores[v]:
        menor = valores[v]
in_maior = valores.index(maior)
in_menor = valores.index(menor)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições... ', end = '')
for p, c in enumerate(valores):
    if maior == c:
        print(f'{p}...', end = '')
print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for p, c in enumerate(valores):
    if menor == c:
        print(f'{p}...',end = '')
