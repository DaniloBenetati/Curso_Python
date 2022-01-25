from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6), # criação de dicionario para os jogos de cada jogador
}
ranking = dict() # criando de dicionario para o ranking
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(0.5)