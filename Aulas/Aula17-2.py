teste = list() # crição de lista
print('Cópias de listas para outra lista')
teste.append('Gustavo')
teste.append(40)
galera = list() # criação de mais uma lista
galera.append(teste[:]) # cópia da lista teste para dentro de outra lista usando [:] para copiar
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera) # mostra duas listas de dentro de uma lista geral
print() # espaço
print('Exemplo de exibição de lista dentro de outra lista')
grupo = [['João', 19], ['Ana', 33], ['Jaqueline', 13], ['Maria', 45]]
print(grupo) # exibe todo o grupo
print(grupo[2]) # exibe o grupo da lista 2 por completo
print(grupo[3][0]) # exibe o grupo 3 na posição 0 no caso o nome "Maria"
print(grupo[1][1]) # exibe o grupo 1 na posição 1 no caso a idade "33"
print() # espaço

print('Exibindo lista dentro de outras listas com for ')
for pessoa in grupo:
    print(pessoa) # exibe o grupo alinhado em nome e idade
print()
for pessoa in grupo:
    print(pessoa[0]) # exibe o grupo apenas pela posição do nome que é [0]
print()
for pessoa in grupo: # exibe o grupo apenas pela posição da idade que é [1]
    print(pessoa[1])
print()
for pessoa in grupo:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade') # usando lista dentro de outra lista para mostrar os resultados
print()
print('Crindo, copiando e limpando lista')

pes = list()
dado = list()
totmaior = totmenor = 0
for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pes.append(dado[:]) # criando um cópia da lista dados para pes
    dado.clear() # limpando a lista dados depois de copiar acima
for p in pes:
    if p[1] >= 21:
        print(f'{p[0]} é maior de ídade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menor de idade.')