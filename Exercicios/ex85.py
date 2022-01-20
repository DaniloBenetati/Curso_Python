lista = list()
pares = list()
impares = list()

for c in range(1, 8):
    lista.append(int(input(f'Digite o {c}º valor: ')))
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    lista.clear() # limpando lista de suporte
pares.sort()
impares.sort()
print(f'{"Resultado":=^50}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')