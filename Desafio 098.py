from time import sleep
def contador(i, f, p):
    print('-='*40)
    print(f'Contagem de {i} até {f} em {p}')
    if p == 0:
        p = 1
        if i > f:
            for c in range(i, f - 1, -p):
                print(f'{c} ',end='', flush=True)
                sleep(0.5)
            print('FIM!')
        if i > f and p < 0:
            for c in range(i, f - 1, p):
                print(f'{c} ',end='',flush=True)
                sleep(0.5)
            print('FIM!')
        else:
            for c in range(i, f + 1, p):
                print(f'{c} ',end='',flush=True)
                sleep(0.5)
            print('FIM!')
    else:
        if i > f:
            for c in range(i, f - 1, -p):
                print(f'{c} ',end='',flush=True)
                sleep(0.5)
            print('FIM!')
        if i > f and p < 0:
            for c in range(i, f - 1, p):
                print(f'{c} ',end='',flush=True)
                sleep(0.5)
            print('FIM!')
        else:
            for c in range(i, f + 1, p):
                print(f'{c} ',end='',flush=True)
                sleep(0.5)
            print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
