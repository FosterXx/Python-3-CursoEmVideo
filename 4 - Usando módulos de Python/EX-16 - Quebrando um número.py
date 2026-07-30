# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import floor

num = float(input("\nDigite um número real (ex: 6.127): "))

print(f"\nO número {num} tem a parte inteira {floor(num)}\n")
