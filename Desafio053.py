frase = str(input('Digite uma palavra:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1 ):
    inverso += junto[letra]
if inverso == junto:
    print('Essa palavra é palíndromo')
else:
    print('A frase digitada não é um palíndromo')