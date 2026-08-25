# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de registro do aproveitamento de cada jogador.

jogador = {}
gols = []

jogadores = []

while True:
    jogador.clear()
    gols.clear()

    jogador['nome'] = str(input("Nome: ")).strip().title()

    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    for p in range (1,partidas+1):
        gols.append(int(input(f"Quantas gols na partida {p}: ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:
        next = str(input("Deseja Continuar[Sim/Não]: ")).strip().upper()[0]
        if next in 'SsNn':
            break
    if next in 'Nn':
        break

print()
print("="*45)

print(f"{'N. Registro':<15}{'Jogador':^15}{'Total de Gol':>15}")

for k, v in enumerate (jogadores):
    print("_"*45)
    print(f"{k:^11}{v['nome']:^23}{v['total']:>6}")

print("="*45)

while True:
    registro = int(input("\nDigite o registro do jogador que deseja ver os detalhes (9999 PARA ENCERRAR): "))

    if registro == 9999:
        break

    if registro < len(jogadores):

        print(f"\nLEVANTAMENTO DO JOGADOR {jogadores[registro]['nome']}")
        print(f"O jogador {jogadores[registro]['nome']} jogou {len(jogadores[registro]['gols'])} partidas:")

        for i, v in enumerate(jogadores[registro]['gols']):
            print(f"  - Partida {i+1} - {v} gols")

        print(f"Total de {jogadores[registro]['total']} gols!")

    else:
        print(f"\nNão existe jogador com o registro {registro}!")

    while True:
        next = str(input("\nDeseja Continuar[Sim/Não]: ")).strip().upper()[0]
        if next in 'SsNn':
            break
    if next in 'Nn':
        break
