km = float(input('Quantos km seu carro percorreu: '))
dias = int(input('Quantos dias o carro foi alugado :'))
cost = 60*dias + 0.15*km
print('seu carro percorreu {}km e foi alugado por {} dias logo o preço fica : {:.2f}reais'.format(km,dias, cost))