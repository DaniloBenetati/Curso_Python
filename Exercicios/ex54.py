from datetime import date
anoatual = date.today().year
idade = 0
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = anoatual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} pessoas atingiram a maior idade')
print(f'{menor} pessoas não atingiram a maior idade')

