somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
print('''Programa de Lógica''')
for pessoa in range(1, 5):
    print(f'-------- {pessoa}° PESSOA --------')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo M/F: ')).strip()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade:.0f} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')


