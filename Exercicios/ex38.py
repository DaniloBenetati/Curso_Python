# ler dois números inteiros e verificar qual é o maior ou se são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    maior = n1
    print(f'O primeiro valor é maior.')
elif n2 > n1:
    maior = n2
    print(f'O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
