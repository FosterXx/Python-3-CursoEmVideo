# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, exiba os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for i in range(1,8):
    num = int(input(f"DIgite o {i}° número: "))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f"\nPares: {numeros[0]}\nImpares: {numeros[1]}\n")
