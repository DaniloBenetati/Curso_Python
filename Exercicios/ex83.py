expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append(expre)
    elif simb == ')':
        if len(pilha) > 0:
             pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
