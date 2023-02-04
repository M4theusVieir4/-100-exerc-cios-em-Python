def notas(*num, sit=False):
    resultados = {}
    resultados['total']=len(num)
    pos = maior = menor = soma = média =0
    for pos in range(0, len(num)):
        soma += num[pos]
        if pos == 0:
            maior = num[pos]
            menor = num[pos]
            pos +=1
        if maior < num[pos]:
            maior = num[pos]
            pos += 1
        if menor > num[pos]:
            menor = num[pos]
            pos += 1
    média = soma / len(num)
    resultados['maior'] = maior
    resultados['menor'] = menor
    resultados['média'] = média
    if média > 7:
        resultados['situação'] = 'BOA'
    else:
        resultados['situação'] = 'RUIM'
    return resultados


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)