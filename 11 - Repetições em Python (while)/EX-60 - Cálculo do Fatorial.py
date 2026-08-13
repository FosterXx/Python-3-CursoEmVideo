# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120

# num = int(input("Digite um número: "))

# fatResul = num
# fatRegistro = num

# while num > 1:

#     fatResul = (fatResul * (num-1))

#     num -= 1

# print(f"\nO resultado de {fatRegistro}! = {fatResul}\n")

###############################################################

# Professor Usando Biblioteca:

# from math import factorial

# num = int(input("\nDigite um numero para calcular o fatorial: "))

# fatResul = factorial(num)

# print(f"\nO fatorial de {num}! é {fatResul}!\n")

###############################################################

num = int(input("Digite um número: "))

cont = num
fat = 1

print(f"Calculando {num}! = ",end='')

while cont > 0:

    # Fluflu para ficar A x B x C x D = R;
    print(f"{cont}", end='')
    print(" x " if cont > 1 else " = ", end='')

    # Calculo do Fatorial;
    fat *= cont

    cont -= 1

print(f"{fat}")
