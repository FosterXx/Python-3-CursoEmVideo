# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maiorP = 0.0
menorP = 0.0

for pessoa in range(1,6):
    peso = float(input(f"\nDigite o peso da {pessoa}° pessoa: "))

    if pessoa == 1:
        maiorP = peso
        menorP = peso
    elif peso > maiorP:
        maiorP = peso
    elif peso < menorP:
        menorP = peso

print(f"\nO maior peso registrado foi {maiorP:.2f} KG, e o menor peso foi {menorP:.2f} KG.\n")