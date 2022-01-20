maior = 0
menor = 0
for c in range (0, 5):
    peso = float(input(f'Peso da {c + 1} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg.')
print(f'O menor peso é {menor}kg.')

