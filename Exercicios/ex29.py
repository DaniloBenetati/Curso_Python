# programa que le a velocidade e multa em R$ 7.00 por cada km excedente a 80km

velocidade = int(input('Digite a velocidade que o carro estava: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'\33[31mALERTA DE MULTA! Sua velocidade foi de {velocidade}km, que é acima de 80km.\n\033[m' # \33[31m - 31 muda a cor para vermelha e \033[m anula as cores e estilos
          f'Você tera que pagar R${multa:.2f}.')
else:
    print(f'\33[1:34mParabens! Você está dirigindo a {velocidade}km, que é dentro da velocidade permitida de 80km.') # \33[1:34 - 1 deixar em negrito e 34 muda a cor para azul