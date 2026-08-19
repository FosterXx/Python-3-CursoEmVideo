# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, exiba o conteúdo das três listas geradas.

valores = []
pares = []
impares = []

while True:
    valor = float(input("Digite um valor: "))
    valores.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    next = str(input("\nDeseja Continuar[Sim/Não]: ")).strip()[0]
    if next in 'Nn' or next not in 'NnSs':
        break

print(f"\nValores: {valores}")
print(f"Pares: {pares}")
print(f"Impares: {impares}\n")
