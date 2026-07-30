# Faça um programa em Python que abra e reproduza o audio de um arquivo mp3.

import pygame

pygame.mixer.init() # Inciar o mixer da biblioteca.

pygame.mixer.music.load('Usando módulos de Python/EX-21.mp3') # Carregar a musica adicionada no projeto.
pygame.mixer.music.play() # Tocar a musica.

print("\nPressione ENTER para parar de reproduzir!\n")
input() # Apertar ENTER no terminal ele encerra a reprodução.

# Em relação a correção do Guanabara, ficou diferente pois algumas funcionalidades estão diferentes da epoca que ele gravou o curso para hoje. Mas pesquisei e consegui resolver para o programa rodar perfeitamente.