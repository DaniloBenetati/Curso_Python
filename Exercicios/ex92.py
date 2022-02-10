# importando bibliotecas
from datetime import date

# importanto ano atual
ano_atual = date.today().year

# criação de listas e dicionarios para armazenar os dados
pessoa = dict()
dados = list()

# imput para perguntar o nome, ano de nascimento e carteira de trabalho.
pessoa["nome"] = str(input('Nome: '))
pessoa['ano'] = int(input('Ano de nascimento: '))
pessoa['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

# condição para continuar o preenchimento, caso o mesmo tenha carteira de trabalho
if pessoa['carteira'] != 0:
    pessoa['ano_cont'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Sálario: '))
    pessoa['aposentadoria'] = ano_atual - pessoa["ano"] + ((pessoa['ano_cont'] + 35) - ano_atual) # idade de aposetadoria

# adicionando o dicionario dentro da lista
dados.append(pessoa)

# exibindo as informações
print(dados)
print()
print(f'Nome: {pessoa["nome"]}')
print(f'Idade: {ano_atual - pessoa["ano"]}')
print(f'CPTS: {pessoa["carteira"]}')
print(f'Sálario: {pessoa["salario"]}')
print(f'Aposentadoria com {pessoa["aposentadoria"]} anos')
