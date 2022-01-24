aluno = dict() # criando o dicionario
aluno['nome'] = str(input('Nome: ')) # adcionando valores ao dicionario
aluno['media'] = float(input(f'Média do {aluno["nome"]}')) # adcionando valores ao dicionario
print(f'Média é igual a {aluno["media"]}') # mostrando resultado
if aluno['media'] >= 7:
    print('Situação é igual a \33[1:32mAprovado')
else:
    print('Situação é igual a \33[1:31mReprovado')
