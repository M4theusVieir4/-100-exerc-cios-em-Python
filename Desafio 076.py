print('-'*30)
print('     LISTAGEM DE PREÇOS ')
print('-'*30)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]} ......................R$  ',end='')
    if c % 2 != 0:
        print(f'{lista[c]} \n')
