print('-=-'*20)
primeiro = int(input('Digite o primeiro termo de uma P.A:'))
razão = int(input('Digite a razão da P.A:'))
print('A P.A começará com o valor {} e com a razão {}'.format(primeiro,razão))
print('-=-'*20)
décimo = primeiro +(10-1)*razão
for c in range(primeiro, décimo + razão, razão):
    print(' {} '.format(c), end='→')
