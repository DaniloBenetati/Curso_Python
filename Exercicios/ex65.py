num = cont = soma = maior = menor = media = 0
pausa = 'S'
while pausa in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pausa = str(input('Quer continuar? [S/N]')).strip().upper()
media = soma / cont

print(f'Você digitou {cont} números e a média foi {media:.1f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
