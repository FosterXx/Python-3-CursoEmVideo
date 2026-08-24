# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
jogadores = []
gols = []
totalG = 0

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome: ")).strip().title()

    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    for p in range (1,partidas+1):
        gols.append(int(input(f"Quantas gols na partida {p}: ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:
        next = str(input("Deseja Continuar[Sim/Não]: "))
        

print("="*40)
print(jogador)
print("="*40)

for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")

print("="*40)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas:")

for i, v in enumerate(jogador['gols']):
    print(f"  - Partida {i+1} - {v} gols")

print(f"Total de {jogador['total']} gols!")
