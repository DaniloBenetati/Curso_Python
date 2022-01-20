a = input('Digite algo: ')
# tipos primitivos
print('O tipo primitivo desse valor é', type(a))

# verificar se tem somente espaços
print('Só tem espaços? ',a.isspace())

# verificar se é um número
print('É um número? ',a.isnumeric())

# verificar se  apenas letras
print('É alfabético? ',a.isalpha())

# verificar se tem algum número
print('É um alfanumérico? ',a.isalnum())

# verificar se todas são maiusculas
print('Está em maiusculas? ',a.isupper())

# verificar se todas as minusculas
print('Está em minusculas? ',a.islower())

# verificar se a primeira letra é maiuscula
print('Está capitalizada? ',a.istitle())