primeiro = int(input('Pimeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo = termo + razao
    cont += 1
print('FIM')

