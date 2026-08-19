# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for valor in range(1,6):
    valores.append(float(input(f"Digite o {valor}° numero: ")))

maior = max(valores)
menor = min(valores)

print(f"\nLista: {valores}")

print(f"Maior Valor: {maior} - indice: ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}", end='..')

print(f"\nMenor Valor: {menor} - indice: ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}", end='..')

print("\nFim de Programa!\n")
