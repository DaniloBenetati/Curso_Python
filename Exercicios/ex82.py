lista = []
res = ' '
pares = []
impares = []
# Criação de loop com pause em 'N'
while res != 'N':
    n = int(input('Digite um valor: '))
    lista.append(n) # incluindo números na lista
    res = str(input('Quer continuar? [N/S] ')).strip().upper()[0]
print(f'A lista completa é {lista}')
# criando condição de pares e impares
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
