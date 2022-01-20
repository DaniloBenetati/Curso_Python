lista = []
maior = 0
menor = 0
# criaçao de loop de 5 perguntas
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

    # logica para localizar o maior e o menor da lista com o indice
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior  = lista[c]
        if lista[c] < menor:
            menor = lista[c]

# listagem de todos
print(50*'=')
print(f'Você digitou os valores {lista}')

# localiando os indices dos maiores
print(f'O maior valor digitado foi o {maior} na posição', end=' ')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}...', end=' ')


# localiando os indices dos maiores
print(f'\nO menor valor digitado foi o {menor} na posição',end=' ')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos}...', end=' ')
