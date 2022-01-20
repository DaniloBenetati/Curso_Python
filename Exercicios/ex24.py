# criar um programa que leia o nome de uma cidade e diga se ela começa com o nome "Santo"

cidade = input('Digite o nome de uma cidade: ').upper()
santo = 'SANTO' in (cidade.split()[0])
print(santo)