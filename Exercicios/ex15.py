km = float(input('Quantos km foram percorridos: '))
dias = int(input('Quantidade de dias alugado :'))

valuguel = dias * 60
vkm = km * 0.15
total = valuguel+vkm

print(f'O total a pagar para {dias} dias de locação é de R${valuguel:.2f}.\n'
      f'O total a pagar oara {km}km rodados é de R${vkm:.2f}\n'
      f'Portanto o total a pagar é {total:.2f}.')