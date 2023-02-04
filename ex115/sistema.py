from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastrada','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... até logo!')
        break
    else:
        cabeçalho('Erro!Digite uma opção válida')
    sleep(2)