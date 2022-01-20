from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você pode adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\33[31mMais... Tente mais uma vez.\33[m')
        elif jogador > computador:
            print('\33[31mMenos... Tente mais uma vez.\33[m')
print(f'\33[32mParabens você acertou! Foram necessários {palpites} palpites para vencer')
