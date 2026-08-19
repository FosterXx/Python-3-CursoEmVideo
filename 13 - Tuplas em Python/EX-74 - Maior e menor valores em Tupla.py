#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

# menor = 0
# maior = 0
# numeros = ()

# for i in range (1,6):
#     n = randint(1,10)

#     if i == 1:
#         menor = n
#         maior = n

#     if n < menor:
#         menor = n
#     elif n > maior:
#         maior = n

#     numeros += (n,)

# print(numeros, maior, menor)

###############################################################

# Professor

numeros = (
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
)

print("\nValores Sorteados: ", end='')

for n in numeros:
    print(f"{n}", end=' ')

print(f"\nMaior Valor: {max(numeros)}") # Metodos das Tuplas = MAX E MIN;
print(f"Menor Valor: {min(numeros)}")
