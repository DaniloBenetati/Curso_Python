grupo = list()
pessoas = list()
maiorp = menorp = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(grupo) == 0:
        maiorp = pessoas[1]
        menorp = pessoas[1]
    else:
        if pessoas[1] > maiorp:
            maiorp = pessoas[1]
        elif pessoas[1] < menorp:
            menorp = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear() # limpando lista pessoas
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=-'*24)
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {len(grupo)} pessoas') # descobrindo a quantidade de pessoas com len
print(f'O maior peso foi de {maiorp}kg. Peso de ', end='')
for p in grupo:
    if p[1] == maiorp:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menorp}kg. Peso de ', end='')
for p in grupo:
    if p[1] == menorp:
        print(f'{p[0]}', end=' ')
