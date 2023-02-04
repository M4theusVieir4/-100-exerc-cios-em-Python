def linha(tam = 42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c}- {item}')
        c += 1
        print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
