largura = float(input('Largura: '))
altura = float(input('Altura: '))

# calculo da area
area = largura * altura

# quantidade que 1 litro pinta
litro = 2

tinta = area / litro

print(f'Sua parede tem a dimensão de {largura} x {altura} e sua area é de {area:.2f}m\n'
      f'Para pintar essa parede, você precisara de {tinta:.2f} litros de tinta')
