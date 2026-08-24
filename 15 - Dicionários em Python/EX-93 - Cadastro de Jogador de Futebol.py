# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
totalG = 0

jogador['nome'] = str(input("Nome: ")).strip().title()

partidas = int(input(f"Quantas partidas {jogador['nome']} jogou: "))

for p in range (1,partidas+1):
    gols.append(int(input(f"Quantas gols na partida {p}: ")))

jogador['gols'] = gols[:]

jogador['total'] = sum(gols)

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
