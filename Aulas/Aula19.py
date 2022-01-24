# Dícionarios

# declara um dicionarios podemos usar dict() ou apenas {}
dados = dict()
dados = {'nome':'Pedro','Idade': 18}
print(dados) # exibe dicionario completo

# adcionando itens ao dicionario
dados['Sexo'] = 'M'
print(dados)

# exluindo item do dicionario
del dados['Idade'] # removendo o item idade
print(dados)

# Criando dicionario para guardar nomes de filmes
print() # espaço
filmes = {
    'Titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'Geroge Lucas'
}
print(filmes)
print()
# acessando item
print(filmes.values())
# acessando chaves
print(filmes.keys())
# acessando valores (completo)
print(filmes.items())
print()
# usando os itens na estrutura for
for k, v in filmes.items():
    print(f'O {k} é {v}.')
print()

# tratamento
pessoas = {
    'Nome': 'Danilo',
    'Sexo': 'M',
    'Idade': 31
}
print(pessoas)
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print()
# percorrendo apenas chaves
for key in pessoas.keys():
    print(k)
print()
# percorrendo todos itens
for key, i in pessoas.items():
    print(f'{key} = {i}')
print()

# apagando item do dicionario
del pessoas['Sexo']
for key, i in pessoas.items():
    print(f'{key} = {i}')
print()

# alterando valor do dicionario (Substituindo o nome Danilo por Leandro)
pessoas['Nome'] = 'Leandro'
for key, i in pessoas.items():
    print(f'{key} = {i}')
print()

# criando dicionario dentro de uma lista
brasil = list() # lista brasil
estado1 = {'uf':'São Paulo','sigla':'SP'}
estado2 = {'uf':'Rio de janeiro','sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) # monstrando dicionario completo dentro da lista
print(brasil[1]) # mostrando apenas o item 1 do dicionario dentro da lista
print(brasil[1]['uf']) # exibe a cidade da posição 1 da lista
print(brasil[1]['sigla']) # exibe a sigla da posição 1 da lista

# fazendo cópia de dicionario com o metodo copy()

estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).upper()
    estado['sigla'] = str(input('Sigla do estado: ')).upper()
    pais.append(estado.copy())
print(pais)
print()
# exibindo com o for
for e in pais:
    print(f'{e}')
print()

# exibindo for detalhado
for e in pais:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print()

# exibindo apenas os valores inves da lista completa
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print() # para dar enter após o loop
