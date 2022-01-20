num = 1
while num > 0:
    print(35*'-')
    num = int(input('Quer ver a tubuada de qual valor? '))
    for tabuada in range(1, 11):
        print(f'{num}  x {tabuada:>2} = {tabuada * num}') # alinhamento com f strings
print(f'Fim do Programa')