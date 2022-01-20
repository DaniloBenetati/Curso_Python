km = int(input('Digite quantos Km tem a sua viagem: '))
if km >= 200:
    print(f'O valor cobrado para viagens acima de 200km é de R$0,45 por km rodados.\n'
          f'Portanto o valor da sua passagem será de R${km*0.45:.2f}.')
else:
    print(f'O valor cobrado para viagens abaixo de 200km é de R$0,50 por km rodados.\n'
          f'Portanto o valor da sua passagem será de R${km*0.50:.2f}.')