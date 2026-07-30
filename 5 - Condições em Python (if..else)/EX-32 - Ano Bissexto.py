# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date # Importa modulo

ano = int(input("\n Digite um ano (Digite 0 para calcular o ano atual): ")) # Recebe um ano.

if ano == 0: # Opção exclusiva para usar o ano atual.

    ano = date.today().year # Pega o ano que está no computador.

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Faz as verificações de um ano bissexto.
        print(f"\nO ano {ano} é BISSEXTO!\n") # Imprimi que é bissexto.
    else: # Caso não seja bissexto.
        print(f"\nO ano {ano} não é BISSEXTO!\n") # Imprimi que não é bissexto.
