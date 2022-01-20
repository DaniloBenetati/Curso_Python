print(f'{"":=^30}')
print(f'{"BANCO CURSO PYTHON":=^30}')
print(f'{"":=^30}')
saque = float(input('Que valor você quer sacar? R$'))
total = saque
totced = 0
ced = 50
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0
        totced = 0
        if ced == 0:
            break








