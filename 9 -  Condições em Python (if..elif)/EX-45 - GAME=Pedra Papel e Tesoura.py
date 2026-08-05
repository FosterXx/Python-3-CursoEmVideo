# Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel e Tesoura) com você.

from random import randint
from time import sleep
from os import system

print("=-="*12)
# Jogador..
print("""
Selecione sua Jogada:

[0] - Pedra
[1] - Papel
[2] - Tesoura
""")
jogador = int(input("\nSua Jogada: "))

system('cls') # Limpar terminal;

# Computador..
computador = randint(0,2)

# FluFlu..
sleep(1)
print("\nJo..")
sleep(1)
print("Ken..")
sleep(1)
print("Pô!\n")
print("=-="*12)

# Regras de Negocio;
#############################################
# Jogador jogou Pedra [0]
if jogador == 0 and computador == 2:
    print("""
Jogador jogou Pedra..
Computador jogou Tesoura..

JOGADOR VENCEU!
""")

elif jogador == 0 and computador == 1:
    print("""
Jogador jogou Pedra..
Computador jogou Pepel..

COMPUTADOR VENCEU!
""")
    
elif jogador == 0 and computador == 0:
    print("""
Jogador jogou Pedra..
Computador jogou Pedra..

EMPATE!
""")
#############################################
# Jogador jogou Papel [1]
elif jogador == 1 and computador == 0:
    print("""
Jogador jogou Papel..
Computador jogou Pedra..

JOGADOR VENCEU!
""")
    
elif jogador == 1 and computador == 2:
    print("""
Jogador jogou Papel..
Computador jogou Tesoura..

COMPUTADOR VENCEU!
""")
    
elif jogador == 1 and computador == 1:
    print("""
Jogador jogou Papel..
Computador jogou Papel..

EMPATE!
""")
#############################################
# Jogador jogou Tesoura [2]
elif jogador == 2 and computador == 0:
    print("""
Jogador jogou Tesoura..
Computador jogou Pedra..

COMPUTADOR VENCEU!
""")
    
elif jogador == 2 and computador == 1:
    print("""
Jogador jogou Tesoura..
Computador jogou Papel..

jOGADOR VENCEU!
""")
    
elif jogador == 2 and computador == 2:
    print("""
Jogador jogou Tesoura..
Computador jogou Tesoura..

EMPATE!
""")
#############################################
else:
    print("\nJogada Invalida!\n")

print("=-="*12)
