def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a


    if 16 <= idade < 18 or idade > 65 :
        return f'Com {idade} anos o voto é Opcional'
    if idade < 16:
        return f'Com {idade} anos o voto é negado.'
    else:
        return  f'Com {idade} anos o voto é Obrigatório'


nascimento = int(input('Ano em que nasceu: '))
print(f'{voto(nascimento)}')
