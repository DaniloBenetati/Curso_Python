titulo = 'LOJA SUPER BARATÃO'
rodape = 'FIM DO PROGRAMA'
print(30*'=')
print(f'{titulo:-^30}')
print(30*'=')
soma = mais1000 = maisbarato = 0
while True:
    produtobatato = ''
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$'))
    soma = soma + preco
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preco > 1000:
        mais1000 += 1
    if preco == preco:
        maisbarato = preco
        produtobatato = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            produtobatato = produto
    if resp == 'N':
        break
print(f'{rodape:-^30}')
print(f'O total da compra foi R${soma:.2f}\n'
      f'Temos {mais1000} produtos custando mais de R$1000,00\n'
      f'O produto mais barato foi {produtobatato} que custa R${maisbarato:.2f}')