from random import randint
from time import sleep
cont = 0
lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd_jogos:
    while cont < 6:
        num = randint(1, 60)
        lista.append(num)
        cont += 1
    jogos.append(lista[:])
    tot += 1
print('-=' * 3, f'SORTEANDO {qtd_jogos} JOGOS','=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)