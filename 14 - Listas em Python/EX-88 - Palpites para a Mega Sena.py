# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = []
palpites = []

cartela = int(input("Quantos jogos deseja realizar: "))

while len(jogos) < cartela:

    while len(palpites) < 6:
        num = (randint(1,60))

        while num not in palpites:
            palpites.append(num)

    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()

sleep(1)
for j in range(0,len(jogos)):
    print(f"Jogo {j+1}: {jogos[j]}")
    sleep(1)
