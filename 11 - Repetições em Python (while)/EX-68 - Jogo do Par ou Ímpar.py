# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("\nPAR OU IMPAR\n")

cont = 0

while True:

    # Jogador;
    opJ = ' '
    while opJ not in 'PpIi':
        opJ = str(input("\nPar ou Impar: ")).strip().upper()[0]

    jogador = int(input("Numero: "))

    # Computador;
    pc = randint(1,2)

    resul = pc + jogador

    if resul % 2 == 0:
        if opJ in 'Pp':
            print("Jogador Ganhou!")

            cont += 1
        else:
            print("Jogador Perdeu!")
            break
    else:
        if opJ in 'Ii':
            print("Jogador Ganhou!")
        
            cont += 1
        else:
            print("Jogador Perdeu!")
            break

print(f"\nVitorias Consecutivas: {cont}\n")
