# Tabuado usando for
print('TABUADA')
num = int(input('Digite um numero para saber a sua tabiada: '))
for tabuada in range(1, 11):
    conta = num * tabuada
    print(f' {num} x {tabuada} = {conta}')
print(15*'_')