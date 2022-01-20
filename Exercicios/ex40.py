# programa de calculo de média de nota

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média foi {media}')
if media < 5:
    print(f'Sua média {media:.1f}, portanto você está \33[1:31mREPROVADO\33[m.')
elif media >=5 and media <= 6.9:
    print(f'Sua media foi {media:.1f}, portanto você está en \33[1:33mRECUPERAÇÃO\33[m.')
elif media >=7:
    print(f'Parabens! Sua média foi de {media}, portanto você está \33[1:32mAPROVADO\33[m.')
