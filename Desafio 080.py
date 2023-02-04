lista = []

for count in range(0, 5):
    valor = int(input('Digite um valor: '))
    if count == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adcionado no final da lista')
    else:
        pos = 0
        while pos <= len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adcionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
