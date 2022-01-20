# calculo de preço

preco = int(input('Digite o valor do produto: '))

# condições:
avista = preco * 0.10
cartao = preco * 0.05
cartao2x = preco
cartao3x = preco * 0.20
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cartão
[ 2 ] à vista cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão''')
opcao = int(input('Qual é a opção: '))

if opcao == 1:
    print(f'Sua compra de R${preco:.2f} tera 10% de desconto, portanto vai custar R${preco-avista:.2f}.')
elif opcao == 2:
    print(f'Sua compra de R${preco:.2f} tera 5% de desconto, portanto vai custar R${preco-cartao:.2f}.')
elif opcao == 3:
    print(f'Sua compra de R${preco:.2f} será parcelada em 2x de {cartao2x/2:.2f} SEM JUROS.')
elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    print(f'Sua compra será parcelada em {parcela}x de R${(cartao3x+preco)/parcela:.2f} COM JUROS.')
    print(f'Sua compra de R${preco} vai custar R${cartao3x+preco:.2f} no final')