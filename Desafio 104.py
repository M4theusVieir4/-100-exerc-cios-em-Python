def leiaInt(msg):
   # ok = False
    valor = 0
    while True:
        num=str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
            #ok = True
        else:
            print('Erro digite um número válido.')
        #if ok:
         #   break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')