for c in range(1):
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número:'))
    n3 = int(input('Digite mais um número: '))
    n4 = int(input('Digite o último número: '))
    valores = (n1, n2, n3, n4)

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhum posição')
print(f'Os valores pares digitados foram',end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')


