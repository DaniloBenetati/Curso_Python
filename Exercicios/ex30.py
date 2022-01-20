num = int(input('Digite um numero para saber se ele é PAR ou IMPAR: '))
resultado = num % 2
if resultado == 0:
    print(f'O numero {num} é \33[1:34mPAR\33[m.')
else:
    print(f'O numero {num} é \33[1:36mIMPAR\33[m.')