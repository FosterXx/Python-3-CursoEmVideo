# Quatro jogadores lançam dados com resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter # Novo elemento da aula;

jogadores = []
ranking = []

for j in range(1,5): # Repete 4 vezes;
    nome = input('Jogador: ') # Pega o nome do jogador;
    resultado = randint(1, 6) # Pega o numero sorteado;

    jogador = { # Cria um dicionario e guarda as informações em jogador e resultado;
        'jogador': nome,
        'resultado': resultado
    }

    jogadores.append(jogador) # Adiciona o dict jogador na list jogadores

    print('Jogando dados...')
    sleep(0.5) # Frufru
    print(f'Seu resultado aleatório foi {resultado}!\n')

ranking = sorted(jogadores, key=itemgetter('resultado'), reverse=True) # Cria uma nova lista (ranking) com sorted() a partir de jogadores, key=itemgetter usa o valor da chave 'resultado' como critério de ordenação, o reverse=True define a ordem do maior para o menor;

for i, v in enumerate(ranking): # Acessamos cada indice = i e valor(dicionario) = v dentro da lista;
    print(f"{i+1}° lugar - {v['jogador']} com {v['resultado']}") # Usamos as keys jogador e resultado para pegar os valores dos dict;
