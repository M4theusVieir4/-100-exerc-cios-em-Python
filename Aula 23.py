try:
    a = int(input('Numerador: '))
    b = int(input('Enumerador: '))
    r=a/b
#except Exception as erro:
#    print(f'O problema encontrado foi {erro.__class__}')
except (ValueError,TypeError):
    print('Tivemos problemas com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não enviar os dados.')

else:
    print(f'O resultado é {r:.3f}')
finally:
    print('Volte sempre muito obrigado')