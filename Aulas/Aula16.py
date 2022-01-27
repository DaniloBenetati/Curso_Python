# Tuplas
lanche = ('hanburquer','suco','pizza','pudim')
print(lanche) # exibe todos os itens da tupla
print(lanche[2:]) # exibe do item 2 em diante ('pizza','pudim')
print(lanche[1]) # exibe apenas um itém da tupla que está posição 1 (suco)
print(lanche[-1]) # exibe o ultimo item da lista (pudim)
print(lanche[-2]) # exibe o penultimo item da lista de tras para frente (pizza)
print(lanche[:2]) # exibe do começo até os itens
print(lanche[1:3]) # exibe a lista do 1 ao item 3 ('suco','pizza') porem no python ele nunca considera o ultimo item
print()
# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'refrigerante' / esse comando não funciona, pois a tupla não deixa incluir um item novo

# Estrutura de FOR em tuplas
for comida in lanche: # exibe a lista dos itens
    print(comida)
print()

for comida in range(0, len(lanche)): # iagual ao resultado acima só que usando len
    print(lanche[comida])
print()

for pos, comida in enumerate(lanche): # usando enumerate para mostrar a posição de cada item
    print(f'Posição {pos} = {comida}')
print()

for cont in range(0, len(lanche)): # exbibe a quantidade de itens usando len
    print(cont)
print()
# ordenar tupla com sorted
print(lanche)
print(sorted(lanche)) # ordena em modo alfabético
print()
# junção de tuplas

a = (5,9,7,8)
b = (11,9,2,8,7)
c = a + b # junta de acordo com a selecionada, não soma
print(c)
print(f'A tupla C tem {len(c)} tens') # conta quantos itens tem dentro da tupla
print(f'O número 9 aparece {c.count(9)} vezes na tupla C.') # mostra quantas vezes o item aparece na tupla
print(f'O número 11 aparece na posição {c.index(11)}.') # mostra a posição que o item está
print(f'O segundo nove aparece na posição {c.index(9,2)}.') # mostra a posição da segunda que vez que ele aparece na, pois o padrão é sempre retornar a primeira
print()

# Tuplas podem ser apagadas por inteita
del(c)
print(c)