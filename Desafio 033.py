n1 = float(input('Type a number: '))
n2 = float(input('Type a second number: '))
n3 = float(input('Type a third number: '))
#Checking who is the smaller number
menor = n1
if n2 < n1 and n2 < n3:
    menor= n2
if n3 < n1 and n3 < n2:
    menor = n3
#Cheking who is the large number
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('The most large number is {} and the smaller is {}'.format(maior,menor))