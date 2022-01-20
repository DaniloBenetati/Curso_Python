palavras = ('aviao','maria','carro','onibus','biblia','mesa','cadeira','girafa',
            'controle','mouse','notebook','casa','computador','luzes',)
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')