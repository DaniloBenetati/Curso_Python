matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = sterc = msl = 0
# inserção de dados sem insert ou append
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l,c}]: '))
print('=-'* 40)
# imprimindo o resultado em forma de matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar = spar + matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    sterc = sterc + matriz[l][2]
print(f'A soma dos valores da tereceira coluna é {sterc}')
for c in range(0, 3):
    if c == 0:
        msl = matriz[1][c]
    elif matriz[1][c] > msl:
        msl = matriz[1][c]
print(f'O maior valor da segunda linha é {msl}')

