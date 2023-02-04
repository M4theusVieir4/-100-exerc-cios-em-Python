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




