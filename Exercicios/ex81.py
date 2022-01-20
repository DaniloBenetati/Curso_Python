lista = []
res = ' '
while res != 'N':
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.') # contagem de vezes que p número foi digitado
print(f'Os valores em ordem decrescentes são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')