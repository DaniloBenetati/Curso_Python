# faça um programa que leia o nome completo de uma pessoa, mostrando apenas o primeiro e o ultimo
nome = input('Digite seu nome completo: ')
primeiro = nome.split()[0]
print(f'primeiro nome = {primeiro}')
ultimo = nome.split()
ultimo2 = ultimo[len(ultimo)-1]
print(f'ultimo nome = {ultimo2}')