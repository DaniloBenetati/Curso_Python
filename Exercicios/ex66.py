num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break # ele quebra o loop antes da linha 6
    cont +=1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')