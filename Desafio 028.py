from random import randint
from time import sleep
computer = randint(0, 5) #make the computer think
print('-=-'*20)
print('I will think in a number between 0 and 5. try guess...')
print('-=-'*20)
player = int(input('What number I thought?')) #Player try guess
print('Processing...')
sleep(3)
if player == computer :
    print('Congratulation! You beat me!')
else:
    print('I win! i thought in the number {} and not in the {} !'.format(computer, player))
