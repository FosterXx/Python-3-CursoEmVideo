# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça ao usuario tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint # Importa modulos das bibliotecas.
from time import sleep 

numero = randint(0,5) # Sorteio do numero (pensar).

resposta = int(input("Tente adivinhar o numero que o sistema 'pensou' de 0 a 5: ")) # Usuario tenta adivinhar.
sleep(2) # Aguarda 2 segundos.

if numero == resposta: # Se o numero adivinhado foi o correto:
    print(f"\nVocê acertou! O numero era {numero}!\n") # Escreva na tela que acertou.
else: # Se o numero adivinhado foi o errado:
    print(f"\nVocê errou! O numero era {numero}!\n") # Escreva na tela que errou.
