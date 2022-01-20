from random import randint
import time
sorteio = int(input('Digite um numero entre 0 e 5: '))
num = randint(0,5)
print('PROCESSANDO...')
time.sleep(0.5)
print(f'\nE o numero sorteado foi: {num}\n')
if num == sorteio:
    print(f'Parabens! Você digitou o número: {sorteio}.')
else:
    print(f'Que pena! Você digitou o número: {sorteio}')