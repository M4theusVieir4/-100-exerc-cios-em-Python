num = int(input('Digite um número inteiro pra ver se é primo: '))
tot = 0
for c in range(1,num + 1):
    if num % c == 0:
        tot += 1

if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')