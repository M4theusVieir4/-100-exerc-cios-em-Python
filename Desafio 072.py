
while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0<= n <= 20:
        break
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número : {extenso[n]}')
