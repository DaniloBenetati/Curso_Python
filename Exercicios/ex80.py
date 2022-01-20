lista = []

# criar loop de 5 repetições de perguntas.
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # localizar primeira posição para a lista e ultima posição
    if c == 0 or n > lista[len(lista)-1]: # se c for primeira posição e n for maior que a última posição
        lista.append(n) # inclua o numero da variavel "n" na lista
        print('Adicioando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # enquanto variavem pos for maior que lista "loop de 5"
            if n <= lista[pos]: # se n for maior ou igual aos numeros da lista entre o primeiro e o ultimo
                lista.insert(pos, n) # insira na posição pos a variavel "n"
                print(f'Adicionado a posição {pos} da lista...')
                break # quebrando o loop do while
            pos += 1
print(f'Os valores digitados em ordem foram {lista}...')