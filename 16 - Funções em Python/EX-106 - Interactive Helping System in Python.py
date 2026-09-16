# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

c = ('\033[m',        # 0 - Sem Cores
     '\033[0;31m',  # 1 - Vermelho
     '\033[0;32m',  # 2 - Verde
     '\033[0;33m',  # 3 - Amarelo
     '\033[0;34m',  # 4 - Azul
     '\033[0;35m',  # 5 - Roxo
     '\033[7;30m'   # 6 - Branco
    )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

    

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP',1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÈ LOGO!',2)

