# Criação de lista vazi
numeros = []
# loop infinito
while True:
    # condição de inclusão na lista
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não adicionado...')

    # Condição de parada do loop
    res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break

# exibir resultados
print(f'Você digitou os valores: {numeros}')





