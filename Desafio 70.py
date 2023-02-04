total = prod_caro = cont = prod_barato= 0
barato = ''
while True:
    print('-'*30)
    print('     LOJA SUPER BARATÃO')
    print('-'*30)
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        prod_caro += 1
    if cont == 1:
        prod_barato == preço
    if preço < prod_barato:
        prod_barato = preço
        barato = nome
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if parada == 'N':
        break
print(f'''O total da compra foi R${total} 
Temos {prod_caro} produtos custando mais de 1000 reais
O produto mais barato foi a {barato} que custou {prod_barato}''')


