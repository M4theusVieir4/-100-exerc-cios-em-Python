from random import randint
print('-='*20)
print('Vamos jogar par ou ímpar?')
print('-='*20)
total = 0
resultado = ''
venceu = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou ímpar?')).upper().strip()[0]
    computador = randint(0, 10)
    total = n + computador
    if total % 2 == 0:
        resultado ='PAR'
    else:
        resultado = 'Ímpar'
    print(f'Você jogou {n} e o computador jogou {computador}. Total de {total} é {resultado}')
    if total % 2 == 0 and pi == 'Í' or total % 2 != 0 and pi == 'P':
        print('VOCÊ PERDEU!')
        break
    else:
        venceu += 1
        print('VOCÊ VENCEU!')
print(f'GAME OVER! Você venceu {venceu} vez.')
