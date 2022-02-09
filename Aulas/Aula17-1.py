# listas
lanche = ['pão', 'suco', 'pizza', 'pudim', ]
print(lanche)

# listas podem ser substituidas
lanche[3] = 'sorvete'  # substituindo o item 3 'pudim' por 'sorvete'
print(lanche)

# adicionar itens novos a listas "append"
lanche.append('chocolate')  # adicionando um itém novo ao final da lista
print(lanche)

# adicionando um itém novo e escolhendo a posição do mesmo com "insert"
lanche.insert(2, 'refrigerante')  # incluindo itém novo na posição 2
print(lanche)

# apagar elementos com o "del"
del (lanche[3])  # apagando o itém 3 'pizza'
print(lanche)

# apagar elementos com o "pop"
lanche.pop()  # o pop apaga sempre o último itém, mas ele aceita parametro também
print(lanche)
lanche.pop(2)  # apagando o itém 2 'refrigerante'
print(lanche)

# apagar elementos com o "remove"
lanche.remove('suco')  # o metodo remove apaga pelo nome do itém
print(lanche)

# apagar itens com remove usando if
if 'pão' in lanche:
    lanche.remove('pão')
print(lanche)
print()  # espaço

# criando listas com "range"
lista = list(range(2, 10))  # cria uma lista de números e coloca em valores
print(lista)
print()

# colocando valores em ordem com sort
valores = [8, 9, 5, 6, 7, 1, 6, 4]
print(valores)
valores.sort()  # os valores ficam em ordem crescente com o sort
print(valores)
valores.sort(reverse=True)  # os valores ficam em ordem reversa
print(valores)
print()

# contanto quantos elementos tem dentro de uma lista com "len"
print(valores)
print(f'Na lista valores existem {len(valores)} itens')
print()

# exibindo uma lista com for
for v in valores:
    print(f'{v}...')  # exibindo em coluna
print()
for valor in valores:
    print(f'{valor}...', end='')  # exibindo em línha
print()
print()

# exibindo o índice com "enumerate"
for i, v in enumerate(valores):
    print(f'Na posição \33[1:31m{i}\33[m encontrei o valor \33[1:32m{v}\33[m')
