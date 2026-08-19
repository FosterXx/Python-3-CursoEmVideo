# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = ()
pares = 0

for n in range(1,5):
    n = float(input(f"\nDigite o {n}° valor: "))

    if n % 2 == 0:
        pares += 1

    numeros += (n,)

print(f"\nNumeros: {numeros}")

print(f"Valor 9 ocorrencias: {numeros.count(9)}")

if 3 in numeros:
    print(f"Valor 3 indice: {numeros.index(3)+1}° posição ou indice {numeros.index(3)}")
else:
    print("Valor 3 não existe na tupla!")

print(f"Pares ocorrencias: {pares}\n")
