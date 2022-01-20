# condiçoes de alistamento militar considerando 18 anos
from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual-ano
print(f'Você tem {idade} anos de idade.')
print('-=' * 52)
if idade < 18:
    print(f'Você ainda não está no periodo de alistamento militar, faltam {18-idade} anos.')
elif idade == 18:
    print(f'Você está no periodo de alistamento militar, compareça a uma junta militar com seus documentos.')
else:
    print(f'Você perdeu o prazo de alistamento em {idade-18} anos, procure uma junta militar para regularizar sua situação')

