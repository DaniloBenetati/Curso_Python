titulo = 'CADASTRE UMA PESSOA'
rodape = 'FIM DO PROGRAMA'
homens = idade = mulher20 = tot18 = 0
while True:
    print(30*'-')
    print(f'{titulo:^30}')
    print(30 * '-')
    Idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo =  str(input('Sexo: [M/F] ')).strip().upper()[0]
    if Idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        print(30 * '-')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(30 * '-')
print(f'{rodape:^30}')
print(30 * '-')
print(f'Total de pessoas com mais de 18 anos: {tot18}\n'
      f'Ao todo temos {homens} homens cadastrados.\n'
      f'E temos {mulher20} com menos de 20 anos')