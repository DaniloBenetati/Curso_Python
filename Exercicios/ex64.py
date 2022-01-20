# solução provisória para flag, confira ex 66 para forma correta
n = 0
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} numeros e a entre eles foi {soma}')