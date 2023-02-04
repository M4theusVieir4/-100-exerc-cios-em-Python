#help(print)
#print(input.__doc__)
#def contador(i, f, p):
 #   """
  #  >Faz uma contagem e mostra na tela
   # :param i:Início
    #:param f:Fim
    #:param p:Passo
    #:return:Sem retorno
    #"""
    #c = i
    #while c <= f:
     #   print(f'{c}',end='')
      #  c += p
#    print('FIM!')
#help(contador)
def soma(a = 0, b = 0, c = 0):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(b=4, c=2)