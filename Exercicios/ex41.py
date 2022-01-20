# classificação de idade
from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Sua idade é {idade} anos')
if idade <= 9:
    print('Portanto sua categoria é MIRIM.')
elif idade >= 10 and idade <= 14:
    print('Portanto sua categoria é INFANTIL.')
elif idade >= 15 and idade <=19:
    print('Portanto sua categoria é JUNIOR.')
elif idade == 20:
    print('Portanto sua categoria é SÊNIOR.')
else:
    print('Portanto sua categoria é MASTER.')