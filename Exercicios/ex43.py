# calculo de IMC corporal
import math
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('-='*20)
print(f'Seu imc é: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do Peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >=30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')