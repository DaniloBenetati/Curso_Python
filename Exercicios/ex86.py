matriz = [[0,0,0],[0,0,0],[0,0,0]]
# inserção de dados sem insert ou append
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l,c}]: '))
print('=-'* 40)
# imprimindo o resultado em forma de matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()