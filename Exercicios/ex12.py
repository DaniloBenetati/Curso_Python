preco = float(input('Digite um valor para saber o seu desconto: '))

#calculo de 5% de desconto
desconto = preco * 0.05
novovalor = preco - desconto

print(f'Para um produto de R${preco:.2f} com desconto de 5% ficara em R${novovalor:.2f} ')