def leiaInt(msg):

    valor = 0
    while True:
        try:
            num=int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o número.')
            return 0
        else:
            valor = num
            return valor


def leiaFloat(msg):
    valor = 0
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o número.')
            return 0
        else:
            valor = num
            return valor



#Programa Principal
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')