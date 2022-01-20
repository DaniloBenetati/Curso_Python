num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro numero: '))
opcao = 0
import time
while opcao != 5:
    print('\33[1:36m=-=-=-Sistema de Escolha-=-=-=\33[m')
    print('''\33[1:34m[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa\33[m''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        somar = num1 + num2
        print(f'{num1} + {num2} = {somar}')
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'{num1} x {num2} = {multiplicar}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior numero digitado foi {maior}')
    elif opcao == 4:
        print('\33[1:36m=-=-=-Sistema de Escolha-=-=-=\33[m')
        print('Informe os números novamente')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro numero: '))
    elif opcao == 5:
        print('Finalizando...')
        time.sleep(0.5)
    else:
        print('Opção Inválida. Tente novamente.')
print('Fim do Programa! Volte sempre!')