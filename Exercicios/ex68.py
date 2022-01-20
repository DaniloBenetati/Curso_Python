from random import randint
soma = 0
resultado = ''
cont = 0
while True:
    print(20 * '-=')
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print(20 * '-=')

    computador = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    escolha = ' ' # tem que ter espaço

    while escolha not in 'PI': # teste de escolha somente P ou I
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end=' ')

    if escolha == 'P' and soma % 2 == 0:
        print('DEU PAR')
        print('Você VENCEU!')
        cont += 1
    elif escolha == 'I' and soma % 2 != 0:
        print('DEU ÍMPAR')
        print('Você VENCEU!')
        cont += 1
    elif escolha == 'P' and soma % 2 != 0:
        print('DEU ÍMPAR')
        print('Você PERDEU!')
        break
    elif escolha == 'I' and soma % 2 == 0:
        print('DEU PAR')
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você veceu {cont} vezes')













