n1 = float(input('Escreva um numero em metros para saber quantos sentimetros tem: '))
centimetros = n1 * 100
milimetros = n1 * 1000
km = n1 / 1000
print(f'{n1} metros corresponde a {centimetros}cm')
print(f'{n1} metros corresponde a {milimetros}mm')
print((f'{n1} metros corresponde a {km}km'))
