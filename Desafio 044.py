from random import randint
player = int(input('Select one number to play: Paper(0), Rock(1), scissors(2): '))
pc = randint(0, 2)
if pc == 1 and player == 0:
    print('You win pc choice rock')
elif pc == 1 and player == 2:
    print('You lost pc choice rock')
elif pc == 2 and player == 0 :
    print('You lost pc choice scissors')
elif pc == 2 and player == 1:
    print('You win pc choice scissors')
elif pc == 0 and player == 1:
    print('You lost pc choice paper')
elif pc == 0 and player == 2:
    print('You win pc choice paper')
elif pc == player:
    print('draw')


