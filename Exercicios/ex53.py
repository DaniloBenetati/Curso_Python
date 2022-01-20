frase = str(input('Digite um frase: ')).strip().upper()
palabras = frase.split() # separar
junto = ''.join(palabras) # juntar
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # "len(junto) - 1" buscou a ultima letra, "-1" até a primeira letra, "-1" voltando uma letra
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')