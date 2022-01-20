from typing import List

nome = str(input('Digite seu nome completo: '))

# nome com todas maiusculas
maiuscula = nome.upper()
print(fmaiuscula)

# nome com todas minusculas
minuscula = nome.lower()
print(minuscula)

# Quantas letras as todo sem considerar os espaços
separado = len(''.join(nome.split()))
print(separado)

# Quantas letras tem no primeiro nome
nome1 = len(nome.split()[0])
print(nome1)