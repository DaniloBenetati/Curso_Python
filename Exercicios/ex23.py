num = int(input('Digite quatro numeros: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Analisando o numero {num}: ')
print(f' unidade: {unidade}\n dezena: {dezena}\n centena: {centena}\n milhar: {milhar}')