def metade(p,f=False):
    r = p/2
    return r if f is False  else moeda(r)


def dobro(p=0,f=False):
    r = p*2
    return r if f is False  else moeda(r)


def aumentar(p=0, t=0,f=False):
    r = p*t/100 + p
    return r if f is False  else moeda(r)


def diminuir(p=0, t=0,f=False):
    r = p - p*t/100
    return r if f is False  else moeda(r)



def moeda(p=0,moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')


def resumo(p=0, ta=0, tr=0):
    print('-'*30)
    print('       RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:    \t{moeda(p):>5}')
    print(f'Dobro do preço:     \t{dobro(p,True):>5}')
    print(f'Metade do preço:    \t{metade(p,True):>5}')
    print(f'{ta} de aumento:    \t\t{aumentar(p,ta,True):>5}')
    print(f'{tr} de redução     \t\t{diminuir(p,tr,True):>5}')

