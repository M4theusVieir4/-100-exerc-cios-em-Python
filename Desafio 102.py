def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num:Número a ser calculado
    :param show:(Opcional)Mostrar ou não a conta
    :return:O valor do Fatorial de um número.
    """
    f = 1
    print('-'*30)
    for c in range(num, 0, -1):
        if show:
            print(f' {c} ',end='')
            if c>1:
                 print('x',end='')
        print('=',end='')
        f *= c
    return f
print(f' {fatorial(5,True)}')
help(fatorial)