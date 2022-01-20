carteira = float(input('Quanto em reais você tem na sua carteira? '))

dolar = 3.27

convert = carteira / dolar

print(f'Você tem U${convert:.2f} dolares considerando R${carteira:.2f} reais em sua carteira')