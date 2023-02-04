
opção = 0
soma = 0
multiplicar = 0
while opção != 5:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    opção = int(input('''    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa 
    :'''))
    if opção == 1:
        soma = num1 + num2
        print('O valor da soma é{}'.format(soma))
    elif opção == 2:
        multiplicar = num1 * num2
        print('O valor da multiplicação é {}'.format(multiplicar))
    elif opção == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é menor que {}'.format(num1, num2))




