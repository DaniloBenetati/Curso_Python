frase = input('Escreva uma frase: ').lower()

# Quantas vezes a letra "a" aparece
a = frase.count('a')
print(f'A letra A aparece {a} vezes na frase')

# Em que posição ela aparece a primeira vez
a1 = frase.find('a')
print(f'A primeira letra A apareceu na posição {a1}')

# Em que posição ela aparece a ultima vez
a2 = frase.rfind('a')
print(f'A últimaa letra A apareceu na posição {a2}')