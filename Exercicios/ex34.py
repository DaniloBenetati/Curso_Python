salario = float(input('Digite o seu sálario para calcular o seu aumento: '))
if salario < 1250:
    print(f'Você ganhou 15% de aumento, portanto seu novo salário é de \33[1:34mR${(salario*0.15)+sa:.2f}\33[m.')
else:
    print(f'Você ganhou 10% de aumento, portanto seu novo salário é de \33[1:34mR${(salario*0.10)+salario:.2f}\33[m.')