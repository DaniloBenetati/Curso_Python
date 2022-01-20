produtos = ('Lapis', 1.50, 'Borracha',1.60,'Lapiseira',4.34,'Caderno',7.30,'Caderno de Desenho',4.55,
            'Cola',3.24,'Estojo',5.30,'Lapis de cor',7.50,'Caneta azul',1.50,'Caneta Vermelha',1.50)
print(40*'-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40*'-')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30} R$', end='')
    else:
        print(f'{produtos[pos]:>5.2f}')
print(40*'-')