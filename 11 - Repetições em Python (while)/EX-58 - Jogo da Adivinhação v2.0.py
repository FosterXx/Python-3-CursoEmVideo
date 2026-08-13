# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

# Apresentação do jogo / Interação;
print("=-="*30)
sleep(0.5)
print("Olá! Eu sou o computador! :b")
sleep(1)
print("Vamos jogar um jogo! Eu pensei em um número de 1 a 10, tente adivinhar! ^~^\n")
sleep(2)

# Computador sorteia numero;
pc = randint(0,10)

# Primeiro palpite do jogador;
jogador = int(input("Seu Palpite: "))

print("=-="*30)
print("Loading..") # Fluflu;

tentativas = 1 # Registrar quantas tentativas até acertar..

while jogador != pc: # Laço de Repetição até acertar;
    print("-"*90)
    sleep(1)

    print(f"\nHeheheh parece que você errou! Não pensei no número {jogador}! *-*")

    if jogador < pc: # Condição para definir uma dica ao Jogador!
        jogador = int(input("\nÉ maior.. Tente Novamente: ")) 
    else:
        jogador = int(input("\nÉ menor.. Tente Novamente: "))

    tentativas +=1

    print("-"*90)
    print("Loading..") # Fluflu;

print("=-="*30)

sleep(1)
print("\nParabénsss! Você acertou! :D")
sleep(0.5)
print(f"\nO número que pensei foi o {pc}!\n\nTentativas: {tentativas}\n")
    
print("=-="*30)

###############################################################


