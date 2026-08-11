# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("\nDigite um numero inteiro: "))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end='') # Cor Amarelo no Texto se Divisivel;
        cont += 1
    else:
        print("\033[31m", end='') # Cor Vermelho no Texto se NÂO Divisivel;

    print(f"{c} ", end='')

print("\033[m") # Cessar Cores no Terminal;

print(f"\nO numero {num} foi divisivel {cont} vezes!")

if cont == 2:
    print("\nO numero é PRIMO!\n")
else:
    print("\nO numero NÂO é PRIMO!\n")

