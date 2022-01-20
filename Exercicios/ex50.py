# ler 6 numeros e somar apenas os pares
somapares = 0
for c in range(1, 7):
    pares = int(input('Digite um número: '))
    if pares % 2 == 0:
        somapares = somapares + pares
print(f'A soma dos pares {somapares}')
