def ajuda(msg):
    while True:
        print('~' * 30)
        print('   SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        fun = str(input('Função ou Biblioteca > '))
        print('~'*30)
        print(f'Acessando o manual do comando "{fun}" ')
        print('~'*30)
        print(help(fun))
        if fun.upper() in 'FIM':
            print('~'*5)
            print('Até logo')
            print('~' * 5)
            break

#Função Principal
manual = ajuda('Função ou Biblioteca > ')
print(ajuda(manual))