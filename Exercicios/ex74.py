from random import randint
menor = maior = 0
sorteio = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(n, end=' ')
    if sorteio == sorteio:
        maior = sorteio
        menor = sorteio
    else:
        if sorteio > maior:
            maior = sorteio
        if sorteio < menor:
            menor = sorteio
print(f'\nO maior valor sorteado foi {max(maior)}'
      f'\nO menor valor sorteado foi {min(menor)}')