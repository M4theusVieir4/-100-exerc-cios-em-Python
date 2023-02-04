def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo')
    m = 0
    for i,v in enumerate(num):
        if i == 0 or m < v:
            m = v
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 1)
maior(0)
