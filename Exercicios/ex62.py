primeiro = int(input('Pimeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais # para começar com o numero indicado no primeiro termo
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print(f'Prgressão finalizada com {total} de termos')