#def fatorial(num=1):
 #   f =1
  #  for c in range(num, 0, -1):
       # f *= c
   # return f


#Função principal
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f' Os resultados são {f1} {f2} {f3}')
def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
n = int(input('Digite um número: '))
if par(n):
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')
