exp = str(input('Digite uma expressão matemática: '))
pilha = []
for sim in exp:
    if sim  == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        if len(pilha) == 0:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')


