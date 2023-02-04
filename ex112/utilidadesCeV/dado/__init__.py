def leiaDinheiro(msg):
    while True:
        dinheiro = str(input(msg)).replace(',','.')
        if dinheiro.strip() =='' or dinheiro.isalpha():
            print('Erro "" é um preço inválido! ')
        else:
            break
    return float(dinheiro)




