print('='*30)
print('         BANCO CEV')
print('='*30)
valor = int(input('Qual valor você quer sacar?: R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= 50:
        total = total -céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de cédulas de R${céd}')
        if céd == 50:
             céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        if total == 0:
            break

