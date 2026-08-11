# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1,7):
    num = int(input("\nDigite um numero inteiro: "))

    if num % 2 == 0:
        soma += num
        cont += 1

print(f"\nVocê informou {cont} numeros pares e a soma dos numeros pares é {soma}.")
