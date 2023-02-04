n = s = 0
while True:
    n = int(input('Digite um número inteiro(999 para encerrar o programa): '))
    if n == 999:
        break
    s += n
print(f'A soma é {s}')
