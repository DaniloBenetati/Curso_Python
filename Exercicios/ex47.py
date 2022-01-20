# soma entre 1 e 500 impares e multiplos de 3
impares = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 ==0:
        impares = impares + c
print(f"A soma dos impares e multiplos de 3 entre 1 e 500 é {impares}.")


