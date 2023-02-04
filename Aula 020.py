#def lin(msg):
 #   print('-'*30)
  #  print(msg)
   # print('-'*30)


#lin('Curso em vídeo')
#lin('Python')
#def soma(a, b):
 #   s = a + b
  #  print(s)


#a = float(input('Digite um número: '))
#b = float(input('Digite outro número: '))
#soma(a,b)
#def contador(* num):
#    for valor in num:
#        print(f'{valor} ',end='')
#    print()

#contador(5, 6, 7)
#contador(7, 8, 9)
#def dobra(lst):
#    pos = 0
#    while pos < len(valores):
#        valores[pos] *= 2
#        pos += 1


#valores = [5, 6, 7, 8, 9]
#dobra(valores)
#print(valores)
def soma(* valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os {valores} temos {s}')

soma(5, 2)
soma(3, 5)
