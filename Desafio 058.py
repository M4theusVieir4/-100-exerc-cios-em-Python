from random import randint
computador = randint(0, 10)
print('Sou seu computador tente advinhar o número que eu pensei...')
tentativas = 0
acerto = False
while not acerto:
        tentativas += 1
        jogador = int(input('Tente digitar o número que o computador pensou:'))
        if jogador == computador:
            acerto = True
        else:
            if jogador < computador:
                print('Mais... Tente mais uma vez')
            elif jogador > computador:
                print('Menos... Tente maisuma vez')

print('Parabéns vc conseguiu em {} tentativas'.format(tentativas))