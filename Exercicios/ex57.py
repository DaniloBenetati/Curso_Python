sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe o sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registado com sucesso')

