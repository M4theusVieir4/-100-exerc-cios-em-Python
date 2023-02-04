#def teste():
 #   x = 8
  #  print(f'Na função teste o n vale {n}')
   # print(f'Na função teste o x vale {x}')
#Função Principal
#n = 2
#print(f'Na função principal o n vale {n}')
#teste()
#print(f'Na função principal o x vale {x}')
#def teste():
 #   n =4
  #  print(f'dentro o n vale {n}')



#n=2
#teste()
#print(f'Fora o N vale {n}')
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a dentro vale {a}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')
#FUNÇÃO PRINCIPAL
a = 5
teste(a)
print(f'a fora vale {a}')

