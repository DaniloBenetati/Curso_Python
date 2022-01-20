# programa de empréstimo bancario residencial onde a parcela não pode exceder 30% do salário
from time import sleep
valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário atual: '))
anos = int(input('Digite quantos anos pretente pagar: '))
meses = anos * 12
parcela = valor_casa / meses
print('-=' * 43)
print(f'Para uma casa de R${valor_casa:.2f}, financiada em {anos} anos a parcela será de R${parcela:.2f}')
print('ANALISANDO O CRÉDITO.....')
sleep(1)
if parcela < salario*0.30:
    print(f'\33[1:34mPARABENS!\33[m\nCrédito aprovado, parcela de R${parcela:.2f} não excede 30% do salário atual de R${salario:.2f}.')
else:
    print(f'\33[1:31mCRÉDITO NEGADO!\33[m \nInfeliste a parcela de R${parcela:.2f} excede 30% do salário atual de R${salario:.2f}')
print('-=' * 43)